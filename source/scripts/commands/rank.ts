import { CommandInteraction, CommandInteractionOption } from '/usr/local/lib/node_modules/discord.js'
import { ISlashCommand } from '../interfaces';

const rank: ISlashCommand =
{
	name: 'rank',
	async execute(interaction: CommandInteraction)
	{
		if (interaction.commandName === 'rank')
		{
			const subcommand: CommandInteractionOption | null = interaction.options.data[0];
			
			// サブコマンドが global の時
			if (subcommand.name === 'global')
			{
				await interaction.reply('this is global');
			}
			
			// サブコマンドが local の時
			if (subcommand.name === 'local')
			{
				await interaction.reply('this is local');
			}

			// サブコマンドが privacy の時
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

module.exports = rank;