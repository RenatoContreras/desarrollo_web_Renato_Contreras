package tarea.web.tarea4.services;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

import tarea.web.tarea4.models.Aviso;

import tarea.web.tarea4.models.AvisoRepository;



@Service
public class AppService {
    
    @Autowired
    private AvisoRepository avisoRepository;
    
    public List<Aviso> obtenerTodosLosAvisos() {
        return avisoRepository.findAllWithComunaAndNotas();
    }
}
