import fs from 'fs';

export namespace BOT_CONSTANTS
{
	// bot の root ディレクトリ
	export const CWD:		string	= '/usr/srb4';
	
	// bot の token
	export const TOKEN:		string	= '';
	
	// bot アカウントの ID
	export const CLIENT_ID:	string	= '957222994927816745';
	
	//  開発用　guild のID
	export const GUILD_ID:	string	= '950792504326897774';


	const dir: string = `${BOT_CONSTANTS.CWD}/slash-commands`;
	const files: Array<string> = fs.readdirSync(dir).filter((file) => { return fs.statSync(`${CWD}/slash-commands/${file}`).isFile() && /.*\.json$/.test(file); });
	let commands: Array<any> = [];
	for(const file of files) { commands.push(JSON.parse(fs.readFileSync(`${dir}/${file}`, 'utf-8'))); }

	// アプリケーションコマンドのリスト
	export const COMMANDS:	Array<string> = commands;
}