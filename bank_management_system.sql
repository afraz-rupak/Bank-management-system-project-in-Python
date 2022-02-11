-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 16, 2021 at 01:00 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank_management_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `Name` varchar(50) DEFAULT NULL,
  `Account_NO` int(11) NOT NULL,
  `Account_Pass` varchar(20) DEFAULT NULL,
  `DoB` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Phone_No` varchar(50) DEFAULT NULL,
  `Opening_Balance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`Name`, `Account_NO`, `Account_Pass`, `DoB`, `Address`, `Phone_No`, `Opening_Balance`) VALUES
('Subrina', 201, '1234', '24/12/1999', 'Dhanmondi', '01818965303', 5000),
('Afroza', 202, '1010', '5/12/1997', 'Chadpur', '01818965303', 1000),
('Nusrat', 203, '9012', '12/10/2010', 'Chittagong', '10238434', 12000);

-- --------------------------------------------------------

--
-- Table structure for table `amount`
--

CREATE TABLE `amount` (
  `Name` varchar(50) DEFAULT NULL,
  `Account_No` varchar(50) DEFAULT NULL,
  `Balance` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `amount`
--

INSERT INTO `amount` (`Name`, `Account_No`, `Balance`) VALUES
('Subrina', '201', 8000),
('Afroza', '202', 3500),
('Nusrat', '203', 12000),
('Nusrat', '9712', 900);

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `B_Id` varchar(11) NOT NULL,
  `B_Name` varchar(60) DEFAULT NULL,
  `B_loc` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`B_Id`, `B_Name`, `B_loc`) VALUES
('09', 'Pahartoli', 'Pahartoli'),
('1', 'Agrabad', 'Agrabad #123'),
('11', 'PQR', 'shukrabad'),
('2', 'Alkoron', 'Alkoron 2'),
('21', 'Agrabad', 'Agrabad'),
('51', 'Dhanmondi', 'xyz'),
('73', 'Halisahar', 'Halishar 345'),
('77', 'EPZ', 'EPZ 11'),
('81', 'Sadarghat', 'Sadarghat 5');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `Loan_Id` int(11) NOT NULL,
  `Loan_Type` varchar(50) DEFAULT NULL,
  `Amount` int(11) DEFAULT NULL,
  `B_Id` varchar(11) DEFAULT NULL,
  `Account_No` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`Loan_Id`, `Loan_Type`, `Amount`, `B_Id`, `Account_No`) VALUES
(1, 'Student Loan', 1000, '1', 201),
(202, 'Personal Loan', 5000, '1', 202),
(203, 'Auto Loan', 1000, '1', 202);

-- --------------------------------------------------------

--
-- Table structure for table `log_info`
--

CREATE TABLE `log_info` (
  `Account_No` int(25) DEFAULT NULL,
  `Account_Pass` varchar(25) DEFAULT NULL,
  `Account_Type` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log_info`
--

INSERT INTO `log_info` (`Account_No`, `Account_Pass`, `Account_Type`) VALUES
(201, '1234', 'Officer'),
(202, '1010', 'Customer'),
(203, '9012', 'Admin'),
(9712, '1234', 'Customer'),
(9713, '1030', 'Customer');

-- --------------------------------------------------------

--
-- Table structure for table `tran_details`
--

CREATE TABLE `tran_details` (
  `User_id` int(11) DEFAULT NULL,
  `T_date` varchar(30) DEFAULT NULL,
  `T_details` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tran_details`
--

INSERT INTO `tran_details` (`User_id`, `T_date`, `T_details`) VALUES
(1, '31/07/2021', 'deposited at 18:01:51'),
(1, '31/07/2021', 'deposited at 18:08:31'),
(1, '31/07/2021', '1000 withdrawed at 19:26:20'),
(1, '31/07/2021', 'transfered at 19:29:03'),
(1184, '09/08/2021', '1000 deposited at 20:24:21'),
(1, '09/08/2021', '1000 deposited at 20:24:58'),
(1, '15/08/2021', '1000 deposited at 00:37:38'),
(202, '16/08/2021', '1000 withdrawed at 01:57:11'),
(202, '16/08/2021', '1000 transfered at 02:07:28'),
(202, '16/08/2021', '1000 transfered at 02:08:51'),
(202, '16/08/2021', '1000 transfered at 02:10:51'),
(202, '16/08/2021', '1000 withdrawed at 02:14:59'),
(202, '16/08/2021', '500 withdrawed at 02:17:20'),
(202, '16/08/2021', '1000 deposited at 04:14:37');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`Account_NO`);

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`B_Id`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`Loan_Id`),
  ADD KEY `B_Id` (`B_Id`),
  ADD KEY `Account_No` (`Account_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `Account_NO` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9715;

--
-- AUTO_INCREMENT for table `loan`
--
ALTER TABLE `loan`
  MODIFY `Loan_Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=204;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `loan`
--
ALTER TABLE `loan`
  ADD CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`B_Id`) REFERENCES `branch` (`B_Id`) ON DELETE NO ACTION,
  ADD CONSTRAINT `loan_ibfk_2` FOREIGN KEY (`Account_No`) REFERENCES `account` (`Account_NO`) ON DELETE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
