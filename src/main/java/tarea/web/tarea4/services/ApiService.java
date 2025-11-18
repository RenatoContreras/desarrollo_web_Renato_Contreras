package tarea.web.tarea4.services;

//import java.util.HashMap;
//import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import jakarta.transaction.Transactional;
import tarea.web.tarea4.models.NotaRepository;
import tarea.web.tarea4.models.AvisoRepository;
import tarea.web.tarea4.models.Nota;
import tarea.web.tarea4.models.Aviso;




@Service
public class ApiService {
    
    @Autowired
    private NotaRepository notaRepository;
    
    @Autowired
    private AvisoRepository avisoRepository;
    
    @Transactional
    public Nota agregarNota(Integer avisoId, Integer nota) {
        if (nota < 1 || nota > 7) {
            throw new IllegalArgumentException("La nota debe estar entre 1 y 7");
        }
        
    if (!avisoRepository.existsById(avisoId)) {
        throw new IllegalArgumentException("Aviso no encontrado");
    }
        
        Nota nuevaNota = new Nota();
        nuevaNota.setAvisoId(avisoId);
        nuevaNota.setNota(nota);
        
        return notaRepository.save(nuevaNota);
    }
    
    public Double obtenerPromedioNotas(Integer avisoId) {
        Aviso aviso = avisoRepository.findById(avisoId)
                .orElseThrow(() -> new IllegalArgumentException("Aviso no encontrado"));
        return aviso.getPromedioNotas();
    }
}
