-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.5.4-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para dbcuentas
CREATE DATABASE IF NOT EXISTS `dbcuentas` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `dbcuentas`;

-- Volcando estructura para tabla dbcuentas.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbcuentas.grupo: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla dbcuentas.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) DEFAULT NULL,
  `grupo` int(11) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `naturaleza` varchar(50) DEFAULT NULL,
  `estado` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_plancuenta_grupo` (`grupo`),
  CONSTRAINT `FK_plancuenta_grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbcuentas.plancuenta: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
