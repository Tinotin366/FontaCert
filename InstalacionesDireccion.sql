-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 14-01-2021 a las 10:07:46
-- Versión del servidor: 10.5.8-MariaDB
-- Versión de PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: Certificados`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla InstalacionesDireccion`
--

CREATE TABLE InstalacionesDireccion` (
  Id_Instalacion` int(5) NOT NULL,
  Id_Direccion` int(5) NOT NULL,
  Id_Via` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  Id_Poblacion` int(6) DEFAULT NULL,
  NombreVia` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  Numero` int(5) DEFAULT NULL,
  Escalera` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  Piso` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  Puerta` varchar(4) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla InstalacionesDireccion`
--

INSERT INTO InstalacionesDireccion` (`Id_Instalacion,  Id_Direccion,  Id_Via,  Id_Poblacion,  NombreVia,  Numero,  Escalera,  Piso,  Puerta`) VALUES
(1, 1, 'Cl', 296400, 'Hinojos, Urb. Stella Blanca', 12, '-', '-', '18A'),
(2, 2, 'Avda', 296400, 'Ramón y Cajal   edf.Las Camelias', 35, '2', '3', 'B'),
(3, 3, 'Cl', 296400, 'Antonio Machado,  edf. Detelina', 6, '3', '7', 'C'),
(4, 4, 'Avda', 135000, 'Primero de Mayo', 29, '-', '-', '-'),
(5, 5, 'Cl', 296500, 'Antequera', 27, '-', '-', '-'),
(6, 6, 'Cl', 296400, 'Miguel Bueno', 5, '-', '4', '3'),
(7, 7, 'Cl', 180060, 'Fontiveros', 34, '-', '-', '-'),
(8, 8, 'Cl', 290080, 'Paquiro', 22, '-', '-', '-'),
(9, 9, 'Avda', 296500, 'De las Margaritas', 41, '-', '2', '-'),
(10, 10, 'Avda', 296500, 'De las Margaritas', 41, '-', '1', '-'),
(11, 11, 'Cl', 334010, 'Doctor Graiño', 7, '-', '-', '-'),
(14, 14, 'Cl', 296402, 'Sauce', 10, '-', '-', '-'),
(15, 15, 'Cl', 296400, 'Sauce', 10, '-', '-', '1'),
(16, 16, 'Cl', 296490, 'Jabega, Edif Torresol', 5, '03', '6', 'C'),
(17, 17, 'Cl', 296402, 'Sauce', 10, '-', '-', '3'),
(18, 18, 'Cl', 296402, 'Sauce', 10, '-', '-', '4'),
(19, 19, 'Cl', 296402, 'Sauce', 10, '-', '-', '5'),
(20, 20, 'Cl', 296402, 'Sauce', 10, '-', '-', '6'),
(21, 21, 'Cl', 296402, 'Sauce', 7, '-', '-', '7'),
(22, 22, 'Cl', 296402, 'Sauce', 10, '-', '-', '8'),
(23, 23, 'Cl', 296402, 'Sauce', 10, '-', '-', '9'),
(24, 24, 'Paseo', 296403, 'Rey de España', 93, '3', '4', 'D'),
(25, 25, 'Paseo', 296403, 'Rey de España', 93, '3', '4', 'C'),
(194, 194, 'Cl', 296490, 'Camino de Coin, edf. Azucena', 39, '-', '7', 'A-1'),
(196, 196, 'Cl', 296400, 'Isabel La Católica', 1, '2', '4', 'A'),
(197, 197, 'Cl', 296400, 'Antiguo Ferrocarril, Edf. Horizontes', 2, '-', '3', 'B'),
(198, 198, 'Cl', 296400, 'Ruedo, parcela S-75', 14, '-', '0', 'A'),
(199, 199, 'Cl', 296400, 'Aragón, Edf. El Rocío', 5, '-', 'Local', '2'),
(200, 200, 'Cl', 296400, 'Mijas, edf. Guadalupe', 7, '-', 'Local', 'A'),
(201, 201, 'Plz', 296400, 'Constitución', 17, '-', '4', '1(A)'),
(202, 202, 'Cl', 296400, 'Juan Breva', 7, '-', '-', 'Alto'),
(319, 319, 'Cl', 296400, 'Antonio Machado', 25, '-', '-', '-'),
(326, 326, 'Avda', 296400, 'Mijas, Edf. La Unión', 44, '1', '1', 'E'),
(806, 806, 'Cl', 296490, 'Hnos. Galán Casero, edf. Ordesa', 13, '-', '2', 'A'),
(1016, 1016, 'Cl', 296400, 'Sauce', 10, '-', '-', '2');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla InstalacionesDireccion`
--
ALTER TABLE InstalacionesDireccion`
  ADD PRIMARY KEY (`Id_Direccion`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
