def handle_response(message) -> str:
    p_message = message.lower() #sees uppercase as lowercase

    #responses for peacemakers

    if p_message == 'selam':
        return 'Selamlar'

    if p_message == 'ğ':
        return 'Ğ'

    if p_message == 'iyi geceler':
        return 'Tatlı rüyalar!'

    if p_message == 'ig':
        return 'Tatlı rüyalar!'


    if p_message == 'la li lu le lo':
        return 'Damn The Patriots.'


    if p_message == '.yayın':
        return 'Yayınlar bu adreslerde! \nhttps://www.twitch.tv/bakruu \n https://www.youtube.com/bakruu'

    if p_message == '.help':
        return 'Yardım için zamanyolcusu.net adresine gidebilirsin! İşte bazı komutlar; \n.yayın \n.minecraft \n.discord \n .davet \n.steam \n.help'

    if p_message == '.minecraft':
        return 'Server ip: "193.122.53.126" \nDomain: zamanyolcusu.net'

    if p_message == '.discord':
        return 'zamanyolcusu.net/discord'
        
    if p_message == '.davet':
        return 'zamanyolcusu.net/discord'
    
    if p_message == '.steam':
        return 'https://steamcommunity.com/groups/peacemakersonline'