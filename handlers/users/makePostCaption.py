def make_post_caption(obj) -> str:
    selling_type = obj.get('sellingType')
    all_players_count = obj.get('allPlayersCount')
    ft_players_count = obj.get('ftPlayersCount')
    im_players_count = obj.get('imPlayersCount')
    legend_players_count = obj.get('legendPlayersCount')
    coins_count = obj.get('coinsCount')
    price = obj.get('price')
    contact = obj.get('contact')

    text = f'♻ Akkaunt: <b>{selling_type}</b>.\n'
    text += f'♻ O\'yinchilar soni: <b>{all_players_count}</b>.\n'
    text += f'♻ FT o\'yinchilar soni: <b>{ft_players_count}</b>.\n'
    text += f'♻ IM o\'yinchilar soni: <b>{im_players_count}</b>.\n'
    text += f'♻ Legend o\'yinchilar soni: <b>{legend_players_count}</b>.\n'
    text += f'♻ Coins soni: <b>{coins_count}</b>.\n\n'

    text += f'💰 Akkaunt narxi: <b>{price}</b>\n'
    text += f'📞 Murojaat etish uchun: <b>{contact}</b>.\n\n'

    text += f'✅ Savdo @PesUzTime adminlari bilan!\n'

    return text
