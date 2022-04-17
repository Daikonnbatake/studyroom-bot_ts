import { CommandInteraction, CommandInteractionOption, MessageActionRow } from 'discord.js'
import { ISlashCommand } from '../interfaces';
import { MessageComponents } from '../utilities/message-components';

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
				if (!option) { test(interaction); }
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

async function test(interaction: CommandInteraction) {
	const actionRow1: MessageActionRow = new MessageActionRow()
		.addComponents(MessageComponents.button('testButton1', 'ボタン1'))
		.addComponents(MessageComponents.button('testButton2', 'ボタン2', 'SECONDARY'))
		.addComponents(MessageComponents.button('testButton3', 'ボタン3', 'SUCCESS'))
		.addComponents(MessageComponents.button('testButton4', 'ボタン4', 'DANGER'));
	
	const column1 = MessageComponents.selectmenuValue('りんご', 'apple', 'りんごかもしれないし、核廃棄物かもしれない', '☢️');
	const column2 = MessageComponents.selectmenuValue('バナナ', 'banana', 'バナナかもしれないし、核廃棄物かもしれない', '☢️');
	const column3 = MessageComponents.selectmenuValue('みかん', 'orange', 'みかんかもしれないし、核廃棄物かもしれない', '☢️');
	
	const actionRow2: MessageActionRow = new MessageActionRow()
		.addComponents(MessageComponents.selectmenu('select1', [column1, column2, column3], '核廃棄物だけ選べ'));
	
		await interaction.reply({content:'this is you', components: [actionRow1, actionRow2]});
}

module.exports = card;