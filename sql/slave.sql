CREATE TABLE `User` (
	`id` INT NOT NULL ,
	`username` VARCHAR(80) NOT NULL UNIQUE,
	`password` VARCHAR(80) NOT NULL,
	`address` VARCHAR(200) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `patient` (
	`id` INT(30) NOT NULL ,
	`name` VARCHAR(40) NOT NULL,
	`blood-type` VARCHAR(4) NOT NULL,
	`diabetes` BOOLEAN NOT NULL,
	`priorOrgan` BOOLEAN NOT NULL,
	`dob` DATE NOT NULL,
	PRIMARY KEY (`id`)
);

