export class MessageDecorate
{
    // value の文字列を太字にする
    static bold(value: string): string { return `**${value}**`; }

    // value の文字列を斜体にする(半角英字のみ)
    static italic(value: string): string { return `_${value}_`; }

    // value の文字列に下線をつける
    static underline(value: string): string { return `__${value}__`; }

    // value の文字列に打消し線をつける
    static strikethrough(value: string): string { return `~~${value}~~`; }

    // value の文字列をスポイラーにする
    static spoiler(value: string): string { return `||${value}||`; }

    // value の文字列をコードブロック(インライン)にする
    static code(value: string): string { return `\`${value}\``; }

    // value の文字列をコードブロックにする
    static codeblock(value: string, language: string = ''): string { return `\`\`\`${language}\n${value}\`\`\``; }
}

export type MD = MessageDecorate;