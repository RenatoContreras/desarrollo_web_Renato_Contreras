package tarea.web.tarea4.models;

import jakarta.persistence.Column;

//import org.springframework.web.multipart.MultipartFile;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
//import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
//import jakarta.persistence.JoinColumn;
//import jakarta.persistence.ManyToOne;
//import jakarta.persistence.OneToMany;
//import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;

//import jakarta.validation.constraints.NotNull;


@Entity
@Table(name = "nota")
public class Nota {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;
    
    @Column(name = "aviso_id")
    private Integer avisoId;
    
    @Column(name = "nota")
    private Integer nota;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "aviso_id", insertable = false, updatable = false)
    private Aviso aviso;
    
    // getters y setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    
    public Integer getAvisoId() { return avisoId; }
    public void setAvisoId(Integer avisoId) { this.avisoId = avisoId; }
    
    public Integer getNota() { return nota; }
    public void setNota(Integer nota) { this.nota = nota; }
    
    public Aviso getAviso() { return aviso; }
    public void setAviso(Aviso aviso) { this.aviso = aviso; }
}
