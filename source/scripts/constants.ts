import fs from 'fs';

import { bot, mysql } from '../conf.json';

export namespace BOT_CONSTANTS
{
	/* conf.json 読み込み */

	// bot の root ディレクトリ
	export const CWD:		string	= '/usr/srb4/source';
	
	// bot の token
	export const TOKEN:		string	= bot.token;
	
	// bot アカウントの ID
	export const CLIENT_ID:	string	= bot.client_id;
	
	//  開発用　guild のID
	export const GUILD_ID:	string	= bot.dev_guild_id;


	const dir: string = `${BOT_CONSTANTS.CWD}/slash-commands`;
	const files: Array<string> = fs.readdirSync(dir).filter((file) => { return fs.statSync(`${CWD}/slash-commands/${file}`).isFile() && /.*\.json$/.test(file); });
	let commands: Array<any> = [];
	for(const file of files) { commands.push(JSON.parse(fs.readFileSync(`${dir}/${file}`, 'utf-8'))); }

	// アプリケーションコマンドのリスト
	export const COMMANDS:	Array<string> = commands;
}