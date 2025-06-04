function notesApp() {
  const marked = window.marked

  return {
    loading: false,
    activeTab: "copy",
    notes: {},
    notification: {
      show: false,
      message: "",
      type: "success",
    },
    autoRefreshInterval: null,

    async init() {
      await this.loadData()
      this.startAutoRefresh()

      // Verificación de notas modificadas
      const modifiedNotes = Object.entries(this.notes).filter(([_, note]) =>
        ["modified_external", "modified_internal"].includes(note.status),
      )

      console.log("Notas modificadas encontradas:", modifiedNotes.length)
      modifiedNotes.forEach(([id, note]) => {
        console.log(`Nota ${id}:`, {
          name: note.original_name,
          status: note.status,
          source: note.modification_source || "unknown",
        })
      })
    },

    startAutoRefresh() {
      // Refrescar datos cada 3 segundos para detectar cambios
      this.autoRefreshInterval = setInterval(async () => {
        await this.loadData(true) // true = silent refresh
      }, 3000)
    },

    stopAutoRefresh() {
      if (this.autoRefreshInterval) {
        clearInterval(this.autoRefreshInterval)
        this.autoRefreshInterval = null
      }
    },

    async loadData(silent = false) {
      try {
        if (!silent) this.loading = true

        const response = await fetch("/get_notes", {
          cache: "no-cache",
          headers: {
            "Cache-Control": "no-cache",
            Pragma: "no-cache",
          },
        })

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`)

        const data = await response.json()
        // console.log("Datos crudos del backend:", data.notes)

        if (!data.notes) throw new Error("Formato de datos incorrecto")

        // Preservar estados de UI existentes
        const previousNotes = { ...this.notes }
        this.notes = {}

        for (const [id, note] of Object.entries(data.notes)) {
          const previousNote = previousNotes[id]

          this.notes[id] = {
            ...note,
            responseContent: previousNote?.responseContent || "",
            showPreview: previousNote?.showPreview || false,
            preview: previousNote?.preview || "",
            processing: previousNote?.processing || false,
            expanded: previousNote?.expanded || false,
          }
        }

        // Detectar cambios importantes solo en refresh no silencioso
        if (!silent) {
          this.detectImportantChanges(previousNotes, this.notes)
        }
      } catch (error) {
        console.error("Error:", error)
        if (!silent) {
          this.showNotification("Error cargando datos: " + error.message, "error")
        }
      } finally {
        if (!silent) this.loading = false
      }
    },

    detectImportantChanges(oldNotes, newNotes) {
      for (const [id, newNote] of Object.entries(newNotes)) {
        const oldNote = oldNotes[id]

        if (oldNote && oldNote.status !== newNote.status) {
          if (newNote.status === "modified_external") {
            this.showNotification(`📝 Nota "${newNote.original_name}" modificada externamente`, "info")
          }
        }
      }
    },

    get stats() {
      const noteValues = Object.values(this.notes)
      return {
        total: noteValues.length,
        copied: noteValues.filter((n) => n.status === "copied").length,
        completed: noteValues.filter((n) => ["completed", "reprocessed"].includes(n.status)).length,
        modified: noteValues.filter((n) => ["modified_external", "modified_internal", "edited"].includes(n.status))
          .length,
      }
    },

    get pendingNotes() {
      return Object.entries(this.notes)
        .filter(([_, note]) => note.status === "pending")
        .reduce((acc, [id, note]) => {
          acc[id] = note
          return acc
        }, {})
    },

    get copiedNotes() {
      return Object.entries(this.notes)
        .filter(([_, note]) => note.status === "copied")
        .reduce((acc, [id, note]) => {
          acc[id] = note
          return acc
        }, {})
    },

    get completedNotes() {
      return Object.entries(this.notes)
        .filter(([_, note]) => ["completed", "reprocessed"].includes(note.status))
        .reduce((acc, [id, note]) => {
          acc[id] = note
          return acc
        }, {})
    },

    get editedNotes() {
      return Object.entries(this.notes)
        .filter(([_, note]) => ["modified_external", "modified_internal", "edited"].includes(note.status))
        .reduce((acc, [id, note]) => {
          acc[id] = note
          return acc
        }, {})
    },

    get notesToProcess() {
      const notes = Object.entries(this.notes).filter(([_, note]) =>
        ["pending", "modified_external", "modified_internal", "edited"].includes(note.status),
      )

      // Ordenar con prioridad a las modificadas
      notes.sort((a, b) => {
        const statusPriority = {
          modified_external: 1,
          modified_internal: 2,
          edited: 3,
          pending: 4,
        }
        return (statusPriority[a[1].status] || 5) - (statusPriority[b[1].status] || 5)
      })

      return Object.fromEntries(notes)
    },

    getStatusText(status) {
      const statusMap = {
        pending: "Pendiente",
        copied: "Copiado",
        completed: "Procesado",
        reprocessed: "Reprocesado",
        modified_external: "⚠️ Modificado (Origen)",
        modified_internal: "⚠️ Modificado (Interno)",
        edited: "Editado",
      }
      return statusMap[status] || status
    },

    getStatusClass(status) {
      return (
        {
          pending: "status-pending",
          copied: "status-copied",
          completed: "status-completed",
          reprocessed: "status-reprocessed",
          modified_external: "status-modified-external",
          modified_internal: "status-modified-internal",
          edited: "status-edited",
        }[status] || "status-pending"
      )
    },

    showNotification(message, type = "success") {
      this.notification = { show: true, message, type }
      setTimeout(() => {
        this.notification.show = false
      }, 5000)
    },

    async copyToClipboard(noteId) {
      const note = this.notes[noteId]
      try {
        note.processing = true
        await navigator.clipboard.writeText(note.content)

        const success = await this.updateNoteStatus(noteId, "copied")
        if (success) {
          note.status = "copied"
          this.showNotification("Nota copiada al portapapeles")
        }
      } catch (error) {
        console.error("Error copying:", error)
        this.showNotification("Error al copiar: " + error.message, "error")
      } finally {
        note.processing = false
      }
    },

    previewResponse(noteId) {
      const note = this.notes[noteId]
      note.showPreview = !note.showPreview
      if (note.showPreview && window.marked) {
        note.preview = window.marked.parse(note.responseContent)
      } else {
        note.preview = note.responseContent
      }
    },

    async pasteResponse(noteId) {
      const note = this.notes[noteId]
      try {
        note.processing = true
        // this.loading = true

        if (!note.responseContent.trim()) {
          throw new Error("El contenido no puede estar vacío")
        }

        const response = await fetch("/process_response", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
          },
          body: JSON.stringify({
            note_id: noteId,
            content: note.responseContent,
          }),
        })

        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.error || `HTTP error! status: ${response.status}`)
        }

        const data = await response.json()
        if (!data.success) {
          throw new Error(data.error || "Error al procesar")
        }

        // Actualizar estado local inmediatamente
        note.status = data.new_status || "completed"
        note.responseContent = "" // Limpiar el contenido
        note.showPreview = false

        this.showNotification("Nota procesada correctamente")

        // Refrescar datos después de un breve delay
        setTimeout(() => this.loadData(true), 500)
      } catch (error) {
        console.error("Error processing response:", error)
        this.showNotification("Error: " + error.message, "error")
      } finally {
        note.processing = false
        this.loading = false
      }
    },

    async updateNoteStatus(noteId, status) {
      try {
        const response = await fetch("/update_status", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
          },
          body: JSON.stringify({ note_id: noteId, status }),
        })

        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.error || `HTTP error! status: ${response.status}`)
        }

        const data = await response.json()
        if (!data.success) {
          throw new Error(data.error || "Error en la actualización")
        }

        return true
      } catch (error) {
        console.error("Error updating status:", error)
        throw error
      }
    },

    async prepareForReprocessing(noteId) {
      const note = this.notes[noteId]
      if (!note) return

      try {
        note.processing = true

        const success = await this.updateNoteStatus(noteId, "pending")

        if (success) {
          // Actualización optimista del estado local
          note.status = "pending"
          note.reprocessCount = (note.reprocessCount || 0) + 1
          note.modification_source = "manual_reprocess"

          this.showNotification("Nota lista para reprocesamiento")
          this.activeTab = "copy"

          // Refrescar datos después de un breve delay
          setTimeout(() => this.loadData(true), 500)
        }
      } catch (error) {
        console.error("Error al preparar para modificar:", error)
        this.showNotification("Error: " + error.message, "error")
      } finally {
        note.processing = false
      }
    },

    // Cleanup cuando se destruye el componente
    destroy() {
      this.stopAutoRefresh()
    },
  }
}


// Cleanup global cuando se cierra la página
window.addEventListener("beforeunload", () => {
  // Detener cualquier intervalo activo
  if (window.notesAppInstance && window.notesAppInstance.autoRefreshInterval) {
    clearInterval(window.notesAppInstance.autoRefreshInterval)
  }
  if (window.notesAppInstance?.destroy) {
    window.notesAppInstance.destroy()
  }
})
