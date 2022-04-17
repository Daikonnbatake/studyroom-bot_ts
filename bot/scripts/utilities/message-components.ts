import { EmojiIdentifierResolvable, MessageButton, MessageButtonStyle, MessageSelectMenu, MessageSelectMenuOptions, MessageSelectOptionData } from "discord.js";

export class MessageComponents
{
    // ボタンのインスタンスを返す
    static button(customID: string, label: string, style?: MessageButtonStyle, url?: string, emoji?: EmojiIdentifierResolvable, disabled?: boolean): MessageButton
    {
        const ret: MessageButton = new MessageButton()
            .setCustomId(customID)
            .setLabel(label)
            .setStyle(style ? style : 'PRIMARY')
            .setURL(url ? url : '')
            .setEmoji(emoji ? emoji : '')
            .setDisabled(disabled ? disabled : false);

        return ret;
    }

    // セレクトメニューのインスタンスを返す
    static selectmenu(customID: string, options: Array<MessageSelectOptionData>, placeholder?: string, max?: number, min?: number, disabled?: boolean): MessageSelectMenu
    {
        const ret: MessageSelectMenu = new MessageSelectMenu()
            .setCustomId(customID)
            .setOptions(options)   
            .setPlaceholder(placeholder ? placeholder : '')
            .setMaxValues(max ? max : 1)
            .setMinValues(min ? min : 0)
            .setDisabled(false);
        
        return ret;
    }

    // セレクトメニューの要素のオブジェクトを返す
    static selectmenuValue(label: string, value: string, description?: string, emoji?: EmojiIdentifierResolvable, isDefault?: boolean): MessageSelectOptionData
    {
        const ret: MessageSelectOptionData =
        {
            label: label,
            value: value,
            description: description ? description : '',
            emoji: emoji ? emoji : '',
            default: isDefault ? isDefault : false
        }

        return ret;
    }
}