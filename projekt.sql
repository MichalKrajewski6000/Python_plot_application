-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 19 Mar 2021, 18:41
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `projekt`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `bilans`
--

CREATE TABLE `bilans` (
  `data` varchar(50) NOT NULL,
  `ilosc` int(6) NOT NULL DEFAULT 0,
  `wartosc` float(8,2) NOT NULL DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `bilans`
--

INSERT INTO `bilans` (`data`, `ilosc`, `wartosc`) VALUES
('2021-03-01', 12, 995.98),
('2021-03-02', 13, 1486.94),
('2021-03-03', 10, 1480.39),
('2021-03-04', 20, 1187.72),
('2021-03-05', 19, 1359.31),
('2021-03-06', 16, 793.94),
('2021-03-07', 15, 1403.67);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `bilans`
--
ALTER TABLE `bilans`
  ADD PRIMARY KEY (`data`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
