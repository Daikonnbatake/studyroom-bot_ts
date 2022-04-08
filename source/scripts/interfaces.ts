import { BaseCommandInteraction } from 'discord.js'

// コマンドのインターフェース
export interface ISlashCommand
{
	// コマンドの名前(この name とjsonで設定した slash-command の name は一致している必要がある)
	name: string;

	// コマンドが呼び出されたときに実行する関数。async で非同期の関数にする必要がある。
	execute(interaction: BaseCommandInteraction): Promise<void>;
}