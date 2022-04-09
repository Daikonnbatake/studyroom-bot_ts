import { CommandInteraction, CommandInteractionOption } from 'discord.js'
import { ISlashCommand } from '../interfaces';

const mcCardGet: ISlashCommand =
{
    name: '自習カードを表示',
    async execute(interaction: CommandInteraction)
    {
        if (interaction.commandName === '自習カードを表示')
        {
            const options: CommandInteractionOption = interaction.options.data[0];
            console.log(options.name);
        }
    }
}

module.exports = mcCardGet;