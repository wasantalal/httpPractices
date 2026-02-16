package main

import (
	"encoding/json"
	"net/http"
)

func main() {
	http.HandleFunc("/name", func(w http.ResponseWriter, r *http.Request) {
		// Set response header to JSON
		w.Header().Set("Content-Type", "application/json")

		// Create response data
		response := map[string]string{
			"message": "Hello Wasan",
		}

		// Encode map to JSON and write to response
		json.NewEncoder(w).Encode(response)
	})

	http.ListenAndServe(":8000", nil)
}
