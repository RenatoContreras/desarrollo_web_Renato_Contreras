package tarea.web.tarea4.models;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface AvisoRepository extends JpaRepository<Aviso, Integer> {
    
    @Query("SELECT a FROM Aviso a LEFT JOIN FETCH a.comuna LEFT JOIN FETCH a.notas ORDER BY a.fechaIngreso DESC")
    List<Aviso> findAllWithComunaAndNotas();
}


