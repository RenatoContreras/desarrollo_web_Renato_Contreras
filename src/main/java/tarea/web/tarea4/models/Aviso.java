package tarea.web.tarea4.models;

import jakarta.persistence.Column;

//import org.springframework.web.multipart.MultipartFile;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;
//import jakarta.validation.constraints.NotNull;

import java.time.LocalDateTime;
import java.util.List;



@Entity
@Table(name = "aviso_adopcion")
public class Aviso {
    @Id
    private Integer id;
    
    @Column(name = "fecha_ingreso")
    private LocalDateTime fechaIngreso;
    
    @Column(name = "sector")
    private String sector;
    
    @Column(name = "nombre")
    private String nombre;
    
    @Column(name = "email")
    private String email;
    
    @Column(name = "celular")
    private String celular;
    
    @Column(name = "tipo")
    private String tipo;
    
    @Column(name = "cantidad")
    private Integer cantidad;
    
    @Column(name = "edad")
    private Integer edad;
    
    @Column(name = "unidad_medida")
    private String unidadMedida;
    
    @Column(name = "fecha_entrega")
    private LocalDateTime fechaEntrega;
    
    @Column(name = "descripcion")
    private String descripcion;
    
    @Column(name = "comuna_id")
    private Integer comunaId;
    
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "comuna_id", insertable = false, updatable = false)
    private Comuna comuna;
    
    @OneToMany(mappedBy = "aviso", fetch = FetchType.LAZY)
    private List<Nota> notas;
    
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    
    public LocalDateTime getFechaIngreso() { return fechaIngreso; }
    public void setFechaIngreso(LocalDateTime fechaIngreso) { this.fechaIngreso = fechaIngreso; }
    
    public String getSector() { return sector; }
    public void setSector(String sector) { this.sector = sector; }
    
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public String getCelular() { return celular; }
    public void setCelular(String celular) { this.celular = celular; }
    
    public String getTipo() { return tipo; }
    public void setTipo(String tipo) { this.tipo = tipo; }
    
    public Integer getCantidad() { return cantidad; }
    public void setCantidad(Integer cantidad) { this.cantidad = cantidad; }
    
    public Integer getEdad() { return edad; }
    public void setEdad(Integer edad) { this.edad = edad; }
    
    public String getUnidadMedida() { return unidadMedida; }
    public void setUnidadMedida(String unidadMedida) { this.unidadMedida = unidadMedida; }
    
    public LocalDateTime getFechaEntrega() { return fechaEntrega; }
    public void setFechaEntrega(LocalDateTime fechaEntrega) { this.fechaEntrega = fechaEntrega; }
    
    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }
    
    public Integer getComunaId() { return comunaId; }
    public void setComunaId(Integer comunaId) { this.comunaId = comunaId; }
    
    public Comuna getComuna() { return comuna; }
    public void setComuna(Comuna comuna) { this.comuna = comuna; }
    
    public List<Nota> getNotas() { return notas; }
    public void setNotas(List<Nota> notas) { this.notas = notas; }
    
    public Double getPromedioNotas() {
        if (notas == null || notas.isEmpty()) {
            return 0.0;
        }
        return notas.stream()
                .mapToInt(Nota::getNota)
                .average()
                .orElse(0.0);
    }
    
}