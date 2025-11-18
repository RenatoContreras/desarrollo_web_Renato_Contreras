package tarea.web.tarea4.controllers;

import java.util.Map;
import java.util.HashMap;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import tarea.web.tarea4.services.ApiService;

import tarea.web.tarea4.models.Nota;



@RestController
@RequestMapping("/api/avisos")
public class ApiController {
    
    @Autowired
    private ApiService apiService;
    
    @PostMapping("/{id}/nota")
    public ResponseEntity<?> agregarNota(@PathVariable Integer id, @RequestBody Map<String, Integer> request) {
        try {
            Integer nota = request.get("nota");
            Nota nuevaNota = apiService.agregarNota(id, nota);
            Double nuevoPromedio = apiService.obtenerPromedioNotas(id);
            
            Map<String, Object> response = new HashMap<>();
            response.put("success", true);
            response.put("nuevaNota", nuevaNota.getNota());
            response.put("nuevoPromedio", nuevoPromedio);
            
            return ResponseEntity.ok(response);
            
        } catch (IllegalArgumentException e) {
            Map<String, Object> response = new HashMap<>();
            response.put("success", false);
            response.put("error", e.getMessage());
            return ResponseEntity.badRequest().body(response);
        }
    }
}
