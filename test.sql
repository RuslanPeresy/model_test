SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
  id int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ИД задания',
  description varchar(255) NOT NULL COMMENT 'Описание задания',
  active tinyint(1) NOT NULL COMMENT 'Флаг активности задания',
  max_days smallint(5) unsigned NOT NULL COMMENT 'Максимальное кол-во дней обзвона',
  max_calls smallint(5) unsigned NOT NULL COMMENT 'Максимальное кол-во звонков в день',
  max_channels smallint(5) unsigned NOT NULL COMMENT 'Максимальное кол-во используемых каналов',
  timeout mediumint(8) unsigned NOT NULL COMMENT 'Минимальный интервал между повторами звонков (в мин.)',
  success_duration smallint(6) NOT NULL COMMENT 'Длительность успешного звонка в сек.',
  trunkid varchar(25) NOT NULL COMMENT 'ИД транка FreePBX',
  start_sound tinyint(1) NOT NULL COMMENT 'Есть ли запись приветствия',
  end_sound tinyint(1) NOT NULL COMMENT 'Есть ли запись информации',
  fax tinyint(1) NOT NULL COMMENT 'Есть ли факс',
  exten varchar(25) NOT NULL COMMENT 'Вн. номер для перевода звонков',
  exten_type tinyint(3) unsigned NOT NULL COMMENT 'Тип переадресации',
  predictive_mode set('preview','none','static','auto') NOT NULL DEFAULT 'none' COMMENT 'Режим предиктивности',
  predictive_percent smallint(6) NOT NULL COMMENT 'Текущий коэффициент предиктивности',
  day_1_start time NOT NULL,
  day_1_end time NOT NULL,
  day_2_start time NOT NULL,
  day_2_end time NOT NULL,
  day_3_start time NOT NULL,
  day_3_end time NOT NULL,
  day_4_start time NOT NULL,
  day_4_end time NOT NULL,
  day_5_start time NOT NULL,
  day_5_end time NOT NULL,
  day_6_start time NOT NULL,
  day_6_end time NOT NULL,
  day_7_start time NOT NULL,
  day_7_end time NOT NULL,
  hidden tinyint(1) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COMMENT='Табица заданий на обзвон';
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;