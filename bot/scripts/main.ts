import { Client, Intents } from 'discord.js';
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

const BOT: Client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_VOICE_STATES] });

// 起動時の処理
BOT.on('ready', () => 
{
	console.log(`起動ｩ～`);
});

// ボイチャ入退室監視
BOT.on('voiceStateUpdate', (oldVoiceState, newVoiceState) =>
{
	let userID = oldVoiceState.id;
	let oldchID = oldVoiceState.channelId;
	let newchID = newVoiceState.channelId;
	let oldch = oldVoiceState.channel;
	let newch = newVoiceState.channel;
	
	// 移動時
	if (oldchID != null && newchID != null && oldch?.guild.id === newch?.guild.id)
	{
		console.log(`退室:    [${Date.now()}] user=${userID}, channel=${oldch?.name}`);
		console.log(`入室:    [${Date.now()}] user=${userID}, channel=${newch?.name}`);
	}

	// 入室時
	else if (oldchID === null && newchID != null)
	{
		console.log(`入室:    [${Date.now()}] user=${userID}, channel=${newch?.name}`);
	}
	
	// 退室時
	else if (oldchID != null && newchID === null)
	{
		console.log(`退室:    [${Date.now()}] user=${userID}, channel=${oldch?.name}`);
	}
});

// コマンド受け付け
BOT.on('interactionCreate', async (interaction) =>
{
	// スラッシュコマンドならこっち
	if (interaction.isCommand())
	{
		const command: ISlashCommand = commands[interaction.commandName];
		try { await command.execute(interaction); }
		catch(e) { console.error(e); }
	}
	
	// 右クリックメニューコマンドならこっち
	else if(interaction.isApplicationCommand())
	{
		const command: ISlashCommand = commands[interaction.commandName];
		try { await command.execute(interaction); }
		catch(e) { console.error(e); }
	}
});

BOT.login(BOT_CONSTANTS.TOKEN);