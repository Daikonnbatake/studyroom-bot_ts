import { Client, Intents } from '/usr/local/lib/node_modules/discord.js';
import fs from 'fs';

import { BOT_CONSTANTS } from './constants';
import { ISlashCommand } from './interfaces';


/* Discord API にスラッシュコマンドを登録する(更新が必要な時はコメントを外す) */
// DiscordAPIにslash-commandをPOST
/*
import { REST } from '/usr/local/lib/node_modules/@discordjs/rest';
import { Routes } from '/usr/local/lib/node_modules/discord-api-types/v9';
const rest = new REST({ version: '9' }).setToken(BOT_CONSTANTS.TOKEN);
(async (): Promise<void> =>
{
	console.log('スラッシュコマンドの登録を開始');
	try { await rest.put(Routes.applicationGuildCommands(BOT_CONSTANTS.CLIENT_ID, BOT_CONSTANTS.GUILD_ID), { body: BOT_CONSTANTS.COMMANDS }); }
	catch(e){ console.error(e); }
})();
*/

// コマンド読み取り
let commands: { [name: string]: ISlashCommand } = {};
const commandFiles: Array<string> = fs.readdirSync(`${BOT_CONSTANTS.CWD}/scripts/commands`).filter(file => file.endsWith('.ts'));
for (const file of commandFiles)
{
	const command: ISlashCommand = require(`./commands/${file}`);
	commands[command.name] = command;
}


/* bot のインスタンス化 & 各種イベント処理 */

const BOT: Client = new Client({ intents: [Intents.FLAGS.GUILDS] });

// 起動時の処理
BOT.on('ready', () => 
{
	console.log(`起動ｩ～`);
});


// コマンド受け付け
BOT.on('interactionCreate', async (interaction) =>
{
	
	if (interaction.isCommand())
	{
		const command: ISlashCommand = commands[interaction.commandName];
		try { await command.execute(interaction); }
		catch(e) { console.error(e); }
	}

	console.log(interaction);


});

BOT.login(BOT_CONSTANTS.TOKEN);