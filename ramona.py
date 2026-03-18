import keep_alive
import interactions
import random
import os

# ---------------------------------------------------
# CONFIGURACIÓN DEL BOT
# ---------------------------------------------------

TOKEN = "MTQzMDIxMzc4MDU1NzY2MDIxMA.GDbS0p.t5OqXdQNKQxZcw3DzoLkjEPVeWzW1Wdn-BTkOQ"
SERVER_ID = 1386808683274440846  # ID de tu servidor

bot = interactions.Client(
    token=TOKEN,
    default_scope=SERVER_ID,
    intents=interactions.Intents.DEFAULT
)

# ---------------------------------------------------
# /hola
# ---------------------------------------------------

@interactions.slash_command(
    name="hola",
    description="DILE HOLA A RAMONA"
)
async def hola(ctx: interactions.SlashContext):
    await ctx.send(f"Hola, {ctx.author.display_name}, soy Ramona")


# ---------------------------------------------------
# /foto
# ---------------------------------------------------

fotos_ramona = [
    "https://i.imgur.com/jGoRvUQ.png", "https://i.imgur.com/86ngRMz.png",
    "https://i.imgur.com/V3KSyki.jpeg", "https://i.imgur.com/Tog6sJv.jpeg",
    "https://i.imgur.com/0MPPnto.jpeg", "https://i.imgur.com/UdBDHRu.jpeg",
    "https://i.imgur.com/S8FJFFu.jpeg", "https://i.imgur.com/sOmIrn9.jpeg",
    "https://i.imgur.com/ZSPR90x.jpeg", "https://i.imgur.com/qkm0KWp.jpeg",
    "https://i.imgur.com/r94DLt9.jpeg", "https://i.imgur.com/ANt68Q7.jpeg",
    "https://i.imgur.com/X6ye8yQ.jpeg", "https://i.imgur.com/ETT5HNJ.jpeg",
    "https://i.imgur.com/KL1RWfR.jpeg", "https://i.imgur.com/fPaTtTK.jpeg",
    "https://i.imgur.com/0Do64pW.jpeg", "https://i.imgur.com/gM3ptD1.jpeg",
    "https://i.imgur.com/eaTmwSr.jpeg", "https://i.imgur.com/OcanpCQ.jpeg",
    "https://i.imgur.com/T9LSjrN.jpeg", "https://i.imgur.com/uvg0Qqm.jpeg",
    "https://i.imgur.com/c5ZZB3S.jpeg", "https://i.imgur.com/JYc5jli.jpeg",
    "https://i.imgur.com/bkClQJ9.jpeg", "https://i.imgur.com/U8uPTFI.jpeg",
    "https://i.imgur.com/vn339Tq.jpeg", "https://i.imgur.com/DDovJUW.jpeg",
    "https://i.imgur.com/wdPt9RB.jpeg", "https://i.imgur.com/sdcBZBZ.jpeg",
    "https://i.imgur.com/lVtOTP9.jpeg", "https://i.imgur.com/mLLnzSD.jpeg",
    "https://i.imgur.com/T19IF34.jpeg", "https://i.imgur.com/2cYE6M7.jpeg",
    "https://i.imgur.com/rD7oS9k.jpeg", "https://i.imgur.com/z1Uqmxw.jpeg",
    "https://i.imgur.com/775V7Vx.jpeg", "https://i.imgur.com/T1ROy7H.jpeg",
    "https://i.imgur.com/AcJlvet.jpeg", "https://i.imgur.com/PjnRHdL.jpeg",
    "https://i.imgur.com/v6XeFtk.jpeg", "https://i.imgur.com/wwPRka7.jpeg",
    "https://i.imgur.com/49Pm9Ly.jpeg", "https://i.imgur.com/02LmJTL.jpeg",
    "https://i.imgur.com/RmTB6Ff.jpeg", "https://i.imgur.com/RwwVKzf.jpeg",
    "https://i.imgur.com/SiZABXk.jpeg", "https://i.imgur.com/1BrQPPu.jpeg",
    "https://i.imgur.com/Lg8JeoH.jpeg", "https://i.imgur.com/VefqdoL.jpeg",
    "https://i.imgur.com/YjFKubk.jpeg", "https://i.imgur.com/kSl9FAG.jpeg",
    "https://i.imgur.com/l0CB0h6.jpeg", "https://i.imgur.com/4M7hfuW.jpeg",
    "https://i.imgur.com/HpdAJzg.jpeg", "https://i.imgur.com/t0mVcXg.jpeg",
    "https://i.imgur.com/OIcWhYV.jpeg", "https://i.imgur.com/VJLx2X5.jpeg",
    "https://i.imgur.com/phNUGoc.jpeg", "https://i.imgur.com/UuNqiYW.jpeg",
    "https://i.imgur.com/Ubb7owz.jpeg"
]

@interactions.slash_command(
    name="foto",
    description="Foto de Ramona"
)
async def foto(ctx: interactions.SlashContext):
    descripciones = [
        "Foto Ramona",
        "RAMONAAAAAAA",
        "*Sonidos de Ramona*",
        "Este bot acabará con mi salud mental",
        "Ramonator 3000 foto",
        "Ramonax",
        "Fotona",
        f"Hay una probabilidad de un {str(100/len(fotos_ramona))[0:5]}% de que salga su marido… ¿te tocó?",
        "Foto de su majestad, La Gran Ramona I.",
        "Ramonica gitanica"
    ]

    embed = interactions.Embed(
        title="📸 Foto de Ramona",
        description=random.choice(descripciones),
        color=0x9b59b6
    )
    embed.set_image(url=random.choice(fotos_ramona))

    await ctx.send(embeds=[embed])

# ---------------------------------------------------
# SISTEMA DE COMBATE
# ---------------------------------------------------

lobby = {"equipo1": [], "equipo2": [], "activo": False}
victorias = {
    "Territorial": {"equipo1": 0, "equipo2": 0},
    "Caótico": {"equipo1": 0, "equipo2": 0}
}
rachas = {"equipo1": 0, "equipo2": 0}

@interactions.slash_command(
    name="combate",
    description="⚔️ Comandos de combate"
)
async def combate(ctx: interactions.SlashContext):
    await ctx.send(
        "⚔️ **Comandos disponibles:**\n"
        "`/combate comenzar`\n"
        "`/combate unirse`\n"
        "`/combate mostrar`\n"
        "`/combate terminar`\n"
        "`/combate contador`\n"
        "`/combate add`\n"
        "`/combate quitar`"
    )

# ------------------ SUBCOMANDOS ------------------

@combate.subcommand(
    sub_cmd_name="comenzar",
    sub_cmd_description="Inicia un nuevo combate"
)
async def comenzar(ctx: interactions.SlashContext):
    if not ctx.author.has_permission(interactions.Permissions.ADMINISTRATOR):
        await ctx.send("🔒 Solo administradores.", ephemeral=True)
        return

    if lobby["activo"]:
        await ctx.send("⚠️ Ya hay un combate activo.")
        return

    lobby["activo"] = True
    lobby["equipo1"] = []
    lobby["equipo2"] = []

    if random.randint(1, 2) == 1:
        lobby["modo_general"] = "Territorial"
        lobby["nombre_modo"] = "Territorial"
        emoji = "<:Territorial:1429868689246650468>"
    else:
        lobby["modo_general"] = "Caótico"
        lobby["nombre_modo"] = random.choice(["Torre", "Pintazonas", "Pez Dorado", "Asalto Almeja"])
        emoji = "<:Caotico:1429868988367638598>"

    r = random.randint(1, 100)
    if r <= 5:
        lobby["tipo"] = "⚡ Bonificación"
        lobby["multiplicador"] = 10
    elif r <= 15:
        lobby["tipo"] = "🔥 Bonificación"
        lobby["multiplicador"] = 5
    else:
        lobby["tipo"] = "🎯 Normal, partida"
        lobby["multiplicador"] = 1

    await ctx.send(
        f"✅ **¡Nuevo combate iniciado!**\n"
        f"👑 Host: {ctx.author.mention}\n\n"
        f"{emoji} **Modo:** {lobby['nombre_modo']} ({lobby['modo_general']})\n"
        f"💥 **Tipo:** {lobby['tipo']} x{lobby['multiplicador']}\n\n"
        f"💬 Usa `/combate unirse` para participar."
    )

@combate.subcommand(
    sub_cmd_name="unirse",
    sub_cmd_description="Únete a un equipo",
    options=[
        interactions.SlashCommandOption(
            name="equipo",
            description="Elige equipo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Equipo 1", value="equipo1"),
                interactions.SlashCommandChoice(name="Equipo 2", value="equipo2"),
            ],
        )
    ]
)
async def unirse(ctx: interactions.SlashContext, equipo: str):
    if not lobby["activo"]:
        await ctx.send("🚫 No hay combate activo.", ephemeral=True)
        return

    if ctx.author.username in lobby["equipo1"] or ctx.author.username in lobby["equipo2"]:
        await ctx.send("⚠️ Ya estás en un equipo.", ephemeral=True)
        return

    if len(lobby[equipo]) >= 4:
        await ctx.send("❌ Ese equipo ya está lleno.", ephemeral=True)
        return

    lobby[equipo].append(ctx.author.username)
    await ctx.send(f"💪 {ctx.author.username} se unió a **{equipo.capitalize()}**.")

@combate.subcommand(
    sub_cmd_name="mostrar",
    sub_cmd_description="Muestra los equipos"
)
async def mostrar(ctx: interactions.SlashContext):
    if not lobby["activo"]:
        await ctx.send("❌ No hay combate activo.")
        return

    embed = interactions.Embed(
        title="⚔️ Lobby de Combate",
        description=(
            f"🟥 **Equipo 1:** {', '.join(lobby['equipo1']) or 'Vacío'}\n"
            f"🟦 **Equipo 2:** {', '.join(lobby['equipo2']) or 'Vacío'}"
        ),
        color=0x9b59b6
    )
    embed.set_footer(text=f"Modo: {lobby['nombre_modo']} • Tipo: {lobby['tipo']}")

    await ctx.send(embeds=[embed])

@combate.subcommand(
    sub_cmd_name="terminar",
    sub_cmd_description="Finaliza el combate",
    options=[
        interactions.SlashCommandOption(
            name="equipo_ganador",
            description="Ganador",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Equipo 1", value="equipo1"),
                interactions.SlashCommandChoice(name="Equipo 2", value="equipo2"),
                interactions.SlashCommandChoice(name="Empate", value="empate")
            ],
        )
    ]
)
async def terminar(ctx: interactions.SlashContext, equipo_ganador: str):
    if not ctx.author.has_permission(interactions.Permissions.ADMINISTRATOR):
        await ctx.send("🔒 Solo administradores.", ephemeral=True)
        return

    if not lobby["activo"]:
        await ctx.send("🚫 No hay combate activo.")
        return

    modo = lobby["modo_general"]

    if equipo_ganador != "empate":
        victorias[modo][equipo_ganador] += lobby["multiplicador"]

        for eq in ["equipo1", "equipo2"]:
            if eq == equipo_ganador:
                rachas[eq] += 1
            else:
                rachas[eq] = 0

        racha_texto = ""
        if rachas[equipo_ganador] >= 2:
            racha_texto = f"\n🔥 **{equipo_ganador.capitalize()} lleva {rachas[equipo_ganador]} victorias seguidas!**"

        resultado = (
            f"🏆 **¡{equipo_ganador.capitalize()} gana!**\n"
            f"🔥 Gana **{lobby['multiplicador']} victorias** en {modo}.{racha_texto}"
        )
    else:
        resultado = "🤝 **Empate.** No se suman victorias."

    lobby["activo"] = False

    await ctx.send(
        f"🏁 **Combate finalizado**\n\n"
        f"🟥 Equipo 1: {', '.join(lobby['equipo1']) or 'Vacío'}\n"
        f"🟦 Equipo 2: {', '.join(lobby['equipo2']) or 'Vacío'}\n\n"
        f"{resultado}"
    )

@combate.subcommand(
    sub_cmd_name="contador",
    sub_cmd_description="Muestra o reinicia victorias",
    options=[
        interactions.SlashCommandOption(
            name="modo",
            description="Modo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Territorial", value="Territorial"),
                interactions.SlashCommandChoice(name="Caótico", value="Caótico"),
            ],
        ),
        interactions.SlashCommandOption(
            name="accion",
            description="Acción",
            type=interactions.OptionType.STRING,
            required=False,
            choices=[
                interactions.SlashCommandChoice(name="Ver", value="ver"),
                interactions.SlashCommandChoice(name="Reset", value="reset"),
            ],
        ),
    ],
)
async def contador(ctx: interactions.SlashContext, modo: str, accion: str = "ver"):
    if not ctx.author.has_permission(interactions.Permissions.ADMINISTRATOR):
        await ctx.send("🚫 Solo administradores.", ephemeral=True)
        return

    if accion == "reset":
        victorias[modo]["equipo1"] = 0
        victorias[modo]["equipo2"] = 0
        await ctx.send(f"🔄 Contadores de **{modo}** reiniciados.")
        return

    embed = interactions.Embed(
        title=f"📊 Victorias - {modo}",
        description=(
            f"🟥 **Equipo 1:** {victorias[modo]['equipo1']}\n"
            f"🟦 **Equipo 2:** {victorias[modo]['equipo2']}"
        ),
        color=0x00ff99
    )
    await ctx.send(embeds=[embed])

@combate.subcommand(
    sub_cmd_name="add",
    sub_cmd_description="Añade victorias",
    options=[
        interactions.SlashCommandOption(
            name="modo",
            description="Modo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Territorial", value="Territorial"),
                interactions.SlashCommandChoice(name="Caótico", value="Caótico"),
            ],
        ),
        interactions.SlashCommandOption(
            name="equipo",
            description="Equipo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Equipo 1", value="equipo1"),
                interactions.SlashCommandChoice(name="Equipo 2", value="equipo2"),
            ],
        ),
        interactions.SlashCommandOption(
            name="cantidad",
            description="Cantidad",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]
)
async def add(ctx: interactions.SlashContext, modo: str, equipo: str, cantidad: int):
    if not ctx.author.has_permission(interactions.Permissions.ADMINISTRATOR):
        await ctx.send("🚫 Solo administradores.", ephemeral=True)
        return

    victorias[modo][equipo] += cantidad
    await ctx.send(f"➕ Añadidas **{cantidad}** victorias a **{equipo.capitalize()}** en {modo}.")

@combate.subcommand(
    sub_cmd_name="quitar",
    sub_cmd_description="Quita victorias",
    options=[
        interactions.SlashCommandOption(
            name="modo",
            description="Modo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Territorial", value="Territorial"),
                interactions.SlashCommandChoice(name="Caótico", value="Caótico"),
            ],
        ),
        interactions.SlashCommandOption(
            name="equipo",
            description="Equipo",
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.SlashCommandChoice(name="Equipo 1", value="equipo1"),
                interactions.SlashCommandChoice(name="Equipo 2", value="equipo2"),
            ],
        ),
        interactions.SlashCommandOption(
            name="cantidad",
            description="Cantidad",
            type=interactions.OptionType.INTEGER,
            required=True
        )
    ]
)
async def quitar(ctx: interactions.SlashContext, modo: str, equipo: str, cantidad: int):
    if not ctx.author.has_permission(interactions.Permissions.ADMINISTRATOR):
        await ctx.send("🚫 Solo administradores.", ephemeral=True)
        return

    victorias[modo][equipo] = max(0, victorias[modo][equipo] - cantidad)
    await ctx.send(f"➖ Quitadas **{cantidad}** victorias a **{equipo.capitalize()}** en {modo}")
# ---------------------------------------------------
# /frase (1/8 mayúsculas)
# ---------------------------------------------------

@interactions.slash_command(
    name="frases",
    description="Ramona te escribe por teclado"
)
async def frases(ctx: interactions.SlashContext):
    letras = "abcdefghijklmnñopqrstuvwxyz "
    cantidad = random.randint(10, 500)

    texto = []
    for _ in range(cantidad):
        letra = random.choice(letras)
        if random.randint(1, 8) == 1:
            letra = letra.upper()
        texto.append(letra)

    await ctx.send("".join(texto))

keep_alive.keep_alive()
bot.start()
