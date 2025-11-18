package tarea.web.tarea4.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
//import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

//import tarea.web.tarea4.models.Aviso;
import tarea.web.tarea4.services.AppService;



@Controller
public class AppController {
    
    @Autowired
    private AppService appService;
    
    @GetMapping("/")
    public String listarAvisos(Model model) {
        model.addAttribute("avisos", appService.obtenerTodosLosAvisos());
        return "index";
    }
}
