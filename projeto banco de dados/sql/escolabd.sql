-- MySQL Script generated by MySQL Workbench
-- Tue Jul 19 14:34:09 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema escola
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema escola
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `escola` DEFAULT CHARACTER SET utf8mb4 ;
USE `escola` ;

-- -----------------------------------------------------
-- Table `escola`.`alunos`
-- -----------------------------------------------------
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


-- -----------------------------------------------------
-- Table `escola`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `escola`.`cursos` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `carga_horaria` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `escola`.`professores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `escola`.`professores` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `valor_hora` INT(10) UNSIGNED NULL DEFAULT NULL,
  `certificados` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `escola`.`turmas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `escola`.`turmas` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `professores_id` INT(11) NOT NULL,
  `cursos_id` INT(10) UNSIGNED NOT NULL,
  `data_inicio` DATE NULL DEFAULT NULL,
  `data_final` DATE NULL DEFAULT NULL,
  `carga_horaria` SMALLINT(5) UNSIGNED NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `turmas_FKIndex1` (`cursos_id` ASC) ,
  INDEX `turmas_FKIndex2` (`professores_id` ASC) ,
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


-- -----------------------------------------------------
-- Table `escola`.`matriculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `escola`.`matriculas` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `turmas_id` INT(10) UNSIGNED NOT NULL,
  `alunos_id` INT(11) NOT NULL,
  `data_matricula` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `matriculas_FKIndex1` (`alunos_id` ASC) ,
  INDEX `matriculas_FKIndex3` (`turmas_id` ASC) ,
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


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
