package tarea.web.tarea4.models;

import jakarta.persistence.Column;

//import java.util.PrimitiveIterator;

//import org.springframework.web.multipart.MultipartFile;

import jakarta.persistence.Entity;
//import jakarta.persistence.FetchType;
//import jakarta.persistence.GeneratedValue;
//import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
//import jakarta.persistence.JoinColumn;
//import jakarta.persistence.ManyToOne;
//import jakarta.persistence.OneToMany;
//import jakarta.persistence.SequenceGenerator;
import jakarta.persistence.Table;

//import jakarta.validation.constraints.NotNull;



@Entity
@Table(name = "comuna")
public class Comuna {
    @Id
    private Integer id;
    
    @Column(name = "nombre")
    private String nombre;
    
    @Column(name = "region_id")
    private Integer regionId;
    
    // getters y setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    
    public Integer getRegionId() { return regionId; }
    public void setRegionId(Integer regionId) { this.regionId = regionId; }
}
