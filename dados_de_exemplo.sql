-- Dados de exemplo do livro Flask de A a Z.
-- Rode este arquivo depois do `alembic upgrade head`, com as tabelas já criadas.
-- Todos os usuários usam a senha 123456.

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS=0;

INSERT INTO `role` (`id`, `name`) VALUES (1,'Admin'),(4,'Cliente'),(2,'Gerente'),(3,'Lojista');

INSERT INTO `category` (`id`, `name`, `description`) VALUES (1,'Calçados','');

INSERT INTO `user` (`id`, `username`, `email`, `password`, `date_created`, `last_update`, `role`, `active`, `recovery_code`) VALUES (2,'admin','admin@email.com','$pbkdf2-sha256$29000$cA4BIKTU2jtHiNG6N2bs/Q$DWkwmruKItSiQaKvbfSrj5G.K3.Yf65cloMIm8yUdeQ','2019-03-02 13:33:00','2019-03-10 15:59:55',1,1,NULL),(4,'gerente','gerente@email','$pbkdf2-sha256$29000$cA4BIKTU2jtHiNG6N2bs/Q$DWkwmruKItSiQaKvbfSrj5G.K3.Yf65cloMIm8yUdeQ','2019-03-07 17:53:00','2019-03-08 09:23:30',2,1,NULL),(5,'lojista','lojista@email','$pbkdf2-sha256$29000$cA4BIKTU2jtHiNG6N2bs/Q$DWkwmruKItSiQaKvbfSrj5G.K3.Yf65cloMIm8yUdeQ','2019-03-07 17:53:00','2019-03-08 09:23:27',3,1,NULL),(6,'usuario','usuario@email','$pbkdf2-sha256$29000$cA4BIKTU2jtHiNG6N2bs/Q$DWkwmruKItSiQaKvbfSrj5G.K3.Yf65cloMIm8yUdeQ','2019-03-07 17:53:00','2019-04-15 16:22:28',4,1,NULL);

INSERT INTO `product` (`id`, `name`, `description`, `qtd`, `image`, `price`, `date_created`, `last_update`, `status`, `user_created`, `category`) VALUES (1,'Tênis','Calçado',20,'',149.90,'2019-03-02 19:32:00','2019-03-02 19:32:00',1,2,1),(2,'Sapato Social','Calçado',40,'',249.90,'2019-03-02 21:17:00','2019-03-02 21:20:26',1,2,1),(3,'Sapatênis','Calçado',200,NULL,350.00,'2019-03-04 12:09:42','2019-03-02 21:20:26',1,2,1),(4,'Sandália','Calçado',30,'',300.00,'2019-03-04 22:53:00','2019-03-04 22:53:00',1,2,1),(5,'Chinelo','Calçado',40,'',1900.00,'2019-03-04 22:54:00','2019-03-04 22:54:00',1,2,1);

SET FOREIGN_KEY_CHECKS=1;
