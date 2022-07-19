

CREATE SCHEMA IF NOT EXISTS `escola` DEFAULT CHARACTER SET utf8 ;
USE `escola` ;

-- -----------------------------------------------------
-- Table `escola`.`alunos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `escola`.`alunos` ;

CREATE TABLE IF NOT EXISTS `escola`.`alunos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `cpf` CHAR(11) NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `fone` CHAR(14) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4;





CREATE TABLE IF NOT EXISTS `escola`.`cursos` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `requisito` VARCHAR(255) NULL DEFAULT NULL,
  `carga_horaria` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
  `preco` DOUBLE UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;




CREATE TABLE IF NOT EXISTS `escola`.`professores` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `valor_hora` INT(10) UNSIGNED NULL DEFAULT NULL,
  `certificados` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;



CREATE TABLE IF NOT EXISTS `escola`.`turmas` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `professores_id` INT(11) NOT NULL,
  `cursos_id` INT(10) UNSIGNED NOT NULL,
  `data_inicio` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `carga_horaria` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `turmas_FKIndex1` (`cursos_id` ASC) VISIBLE,
  INDEX `turmas_FKIndex2` (`professores_id` ASC) VISIBLE,
  CONSTRAINT `turmas_ibfk_1`
    FOREIGN KEY (`cursos_id`)
    REFERENCES `escola`.`cursos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `turmas_ibfk_2`
    FOREIGN KEY (`professores_id`)
    REFERENCES `escola`.`professores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


CREATE TABLE IF NOT EXISTS `escola`.`matriculas` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `turmas_id` INT(10) UNSIGNED NOT NULL,
  `alunos_id` INT(11) NOT NULL,
  `data_matricula` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `matriculas_FKIndex1` (`alunos_id` ASC) VISIBLE,
  INDEX `matriculas_FKIndex3` (`turmas_id` ASC) VISIBLE,
  CONSTRAINT `matriculas_ibfk_1`
    FOREIGN KEY (`alunos_id`)
    REFERENCES `escola`.`alunos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `matriculas_ibfk_2`
    FOREIGN KEY (`turmas_id`)
    REFERENCES `escola`.`turmas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;




CREATE TABLE IF NOT EXISTS `escola`.`responsaveis` (
  `id` INT(11) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `nome` VARCHAR(50) NOT NULL,
  `fone` VARCHAR(14) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `escola`.`responsaveis_has_alunos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `escola`.`responsaveis_has_alunos` ;

CREATE TABLE IF NOT EXISTS `escola`.`responsaveis_has_alunos` (
  `responsaveis_id` INT(11) NOT NULL,
  `alunos_id` INT(11) NOT NULL,
  PRIMARY KEY (`responsaveis_id`, `alunos_id`),
  INDEX `fk_responsaveis_has_alunos_alunos1_idx` (`alunos_id` ASC) VISIBLE,
  INDEX `fk_responsaveis_has_alunos_responsaveis1_idx` (`responsaveis_id` ASC) VISIBLE,
  CONSTRAINT `fk_responsaveis_has_alunos_responsaveis1`
    FOREIGN KEY (`responsaveis_id`)
    REFERENCES `escola`.`responsaveis` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_responsaveis_has_alunos_alunos1`
    FOREIGN KEY (`alunos_id`)
    REFERENCES `escola`.`alunos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
