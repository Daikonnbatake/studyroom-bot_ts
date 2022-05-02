-- DB復旧用SQL

-- `6hdl4_srb3`.study_time definition

CREATE TABLE `study_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `timestamp` bigint(20) unsigned NOT NULL,
  `status` tinyint(1) NOT NULL,
  `cumulative_sum` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `study_time_UN` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- `6hdl4_srb3`.users definition

CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL COMMENT 'discordのUser_ID',
  `privacy_card` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Trueのとき隠す',
  `privacy_rank` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'Trueのとき隠す',
  `badge_acquired` int(11) NOT NULL DEFAULT '7' COMMENT '2進数25桁のbitフラグ',
  `badge_equipe_1` int(11) NOT NULL DEFAULT '0',
  `badge_equipe_2` int(11) NOT NULL DEFAULT '0',
  `badge_equipe_3` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_UN` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- `6hdl4_srb3`.guilds definition

CREATE TABLE `guilds` (
  `id` bigint(20) unsigned NOT NULL,
  `role_control` tinyint(1) NOT NULL DEFAULT '0',
  `is_craziness` tinyint(1) NOT NULL DEFAULT '0' COMMENT '発狂モード切替え',
  `anounce_ch` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `guilds_UN` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- `6hdl4_srb3`.channels definition

CREATE TABLE `channels` (
  `id` bigint(20) unsigned NOT NULL COMMENT 'チャンネルのID',
  `type` tinyint(1) NOT NULL COMMENT 'voiceかtextか(trueならvoice)',
  `rated` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'ランク反映に使用するかどうか',
  PRIMARY KEY (`id`),
  UNIQUE KEY `channels_UN` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;