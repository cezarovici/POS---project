-- Create cadru_didactic table
CREATE TABLE `cadru_didactic` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `nume` VARCHAR(70) NOT NULL,
  `prenume` VARCHAR(70) NOT NULL,
  `email` VARCHAR(100) UNIQUE,
  `grad_didactic` ENUM('Asistent', 'Sef Lucrari', 'Conferentiar', 'Profesor'),
  `tip_asociere` ENUM('Titular', 'Asociat', 'Extern') NOT NULL,
  `afiliere` VARCHAR(255)
);

-- Create student table
CREATE TABLE `student` (
  `id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `nume` VARCHAR(70) NOT NULL,
  `prenume` VARCHAR(70) NOT NULL,
  `email` VARCHAR(100) UNIQUE,
  `ciclu_studii` ENUM('Licenta', 'Master') NOT NULL,
  `an_studiu` INTEGER NOT NULL,
  `grupa` INTEGER NOT NULL
);

-- Create disciplina table
CREATE TABLE `disciplina` (
  `COD` VARCHAR(10) PRIMARY KEY,
  `id_titular` INTEGER,
  `nume_disciplina` VARCHAR(100) NOT NULL,
  `an_studiu` INTEGER NOT NULL,
  `tip_disciplina` ENUM('Impusa', 'Optionala', 'Liber_Aleasa') NOT NULL,
  `categorie_disciplina` ENUM('Domeniu', 'Specialitate', 'Adiacenta') NOT NULL,
  `tip_examinare` ENUM('Examen', 'Colocviu') NOT NULL,
  FOREIGN KEY (`id_titular`) REFERENCES `cadru_didactic` (`id`)
);

-- Insert sample data into cadru_didactic
INSERT INTO `cadru_didactic` (`nume`, `prenume`, `email`, `grad_didactic`, `tip_asociere`, `afiliere`) VALUES
('Popescu', 'Ion', 'ion.popescu@example.com', 'Profesor', 'Titular', 'Universitatea Bucuresti'),
('Ionescu', 'Ana', 'ana.ionescu@example.com', 'Conferentiar', 'Asociat', 'Universitatea Cluj'),
('Marin', 'Radu', 'radu.marin@example.com', 'Sef Lucrari', 'Extern', 'Academia de Studii Economice');

-- Insert sample data into student
INSERT INTO `student` (`nume`, `prenume`, `email`, `ciclu_studii`, `an_studiu`, `grupa`) VALUES
('Popescu', 'Maria', 'maria.popescu@student.example.com', 'Licenta', 2, 101),
('Ionescu', 'George', 'george.ionescu@student.example.com', 'Master', 1, 202),
('Marin', 'Elena', 'elena.marin@student.example.com', 'Licenta', 3, 303);

-- Insert sample data into disciplina
INSERT INTO `disciplina` (`COD`, `id_titular`, `nume_disciplina`, `an_studiu`, `tip_disciplina`, `categorie_disciplina`, `tip_examinare`) VALUES
('MATH101', 1, 'Matematica Aplicata', 1, 'Impusa', 'Domeniu', 'Examen'),
('CS102', 2, 'Introducere in Programare', 1, 'Impusa', 'Specialitate', 'Examen'),
('HIST201', 3, 'Istoria Europei', 2, 'Optionala', 'Adiacenta', 'Colocviu');
