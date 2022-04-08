import { CommandInteraction, CommandInteractionOption } from 'discord.js'
import { ISlashCommand } from '../interfaces';

const card: ISlashCommand =
{
	name: 'card',
	async execute(interaction: CommandInteraction)
	{
		if (interaction.commandName === 'card')
		{
			let subcommand: CommandInteractionOption | null = interaction.options.data[0];
			
			// サブコマンドが get の場合
			if (subcommand.name === 'get')
			{
				// 適切な個数の引数が存在するなら
				if (!subcommand.options) { return; }
				
				const option: CommandInteractionOption = subcommand.options[0];
				if (!option) { await interaction.reply('this is you'); }
				else if (subcommand.options.length != 1) { await interaction.reply('argment error'); }
				else if (option.name === 'user') { await interaction.reply('this is user'); }
				else if (option.name === 'id') { await interaction.reply('this is id'); }
			}
			
			// サブコマンドが badge の場合
			if (subcommand.name === 'badge')
			{
				await interaction.reply('this is badge');
			}
			
			// サブコマンドが privacy の場合
			if (subcommand.name === 'privacy')
			{
				if (!subcommand.options) { return; }
				
				const option: CommandInteractionOption = subcommand.options[0];
				if (option.name === 'status')
				{
					// 引数が true の時
					if (option.value) { await interaction.reply('true!'); }

					// 引数が false の時
					else { await interaction.reply('false!'); }
				}
			}
		}
	}
}

module.exports = card;