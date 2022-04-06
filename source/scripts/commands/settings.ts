import { CommandInteraction, CommandInteractionOption } from '/usr/local/lib/node_modules/discord.js'
import { ISlashCommand } from '../interfaces';

const settings: ISlashCommand =
{
	name: 'settings',
	async execute(interaction: CommandInteraction)
	{
		if (interaction.commandName === 'settings')
		{
			const subcommand: CommandInteractionOption | null = interaction.options.data[0];
			
			// サブコマンドグループが study-room の時
			if (subcommand.name === 'study-room')
			{
				// オプションが null だったら弾いて、以降の options が null でないことを保証する
				if (!subcommand.options){ return; }
				if (!subcommand.options[0].options){ return; }
				
				// サブサブコマンドを取得
				const subsubcommand: CommandInteractionOption | null = subcommand.options[0]
				
				// サブサブコマンドが add の時
				if (subsubcommand.name === 'add')
				{
					if (!subsubcommand.options) { return; }
					
					const option: CommandInteractionOption = subsubcommand.options[0];
					if (option.name === 'voice-channel')
					{
						await interaction.reply('this is add');
					}
				}
				
				// サブサブコマンドが pop の時
				if (subsubcommand.name === 'pop')
				{
					if (!subsubcommand.options) { return; }
				
					const option: CommandInteractionOption = subsubcommand.options[0];
					if (option.name === 'voice-channel')
					{
						await interaction.reply('this is pop');
					}
				}
			}

			// サブコマンドが announce の時
			if (subcommand.name === 'announce')
			{
				if(subcommand.options)
				{
					const option: CommandInteractionOption = subcommand.options[0];
					if (option.name === 'channel')
					{
						await interaction.reply('this is announce');
					}
				}
			}

			// サブコマンドが role の時
			if (subcommand.name === 'role')
			{   
				if(!subcommand.options) { return; }
				
				const option: CommandInteractionOption = subcommand.options[0];
				if (option.name === 'status')
				{
					await interaction.reply('this is announce');
				}
			}
		}
	}
}

module.exports = settings;