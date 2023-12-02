import discord
import sqlite3
import asyncio
import datetime as dt
from discord.ext import commands
from discord.ext import tasks
import scrapping as sp
import tracemalloc

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # Habilita el intent de contenido de mensaje

#Conexion con la base de datos
conn = sqlite3.connect('bot.db')
db = conn.cursor()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='enviar_notificacion')
async def enviar_notificacion(ctx, mensaje):
    # Obtiene el canal de notificaciones 
    canal_notificaciones = discord.utils.get(ctx.guild.channels, name='general')

    if canal_notificaciones:
        # Envía el mensaje al canal de notificaciones
        await canal_notificaciones.send(mensaje)
    else:
        await ctx.send("No se encontró el canal de notificaciones.")

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return  # Evita que el bot responda a sus propios mensajes

    if message.content.startswith('!menu'):
        menu = "Elige una opción:\n1) Documentación\n2) Asistencia\n3) Enviar Notificacion a otro canal\n4) Llenar tabla tareas y semanas\n5) Reminder"
        await message.channel.send(menu)
        
        # Función para esperar una respuesta del usuario
        def check(response):
            return response.author == message.author and response.channel == message.channel

        try:
            response = await bot.wait_for('message', check=check, timeout=20)  # Espera una respuesta durante 20 segundos
            if response.content == '1':
                menu_docs = "Elige a que semana deseas acceder:\n1) Semana 1\n2) Semana 2\n3) Semana 3\n4) Semana 4\n5) Semana 5\n6) Semana 6\n7) Semana 7\n8) Semana 8\n9) Semana 9\n10) Semana 10"
                await message.channel.send(menu_docs)
                respuesta = await bot.wait_for('message', check=check, timeout=20)
                opcion = respuesta.content
                match (opcion):
                    case "1":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 1").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "2":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 2").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "3":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 3").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "4":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 4").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "5":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 5").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "6":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 6").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "7":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 7").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "8":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 8").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "9":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 9").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
                    case "10":
                        data_week = db.execute("SELECT * FROM semanas WHERE id = 10").fetchall()
                        await message.channel.send(f"Tema: {data_week[0][1]}\n Inicia {data_week[0][5]} y finaliza {data_week[0][6]}\n -Documentación extra: {data_week[0][2]}\n -Diapositivas: {data_week[0][3]}\n -Lecture: {data_week[0][4]}")
            
            elif response.content == '4': # funcion para escrapear la pagina web
                # resultados = sp.date_pset()
                menu_date = "Elige que tabla quieres llenar\n1) Tareas\n2) Semanas"
                await message.channel.send(menu_date)
                respuesta = await bot.wait_for('message', check=check, timeout=20)
                opcion = respuesta.content

                match opcion:
                    case "1":
                        pass

                    case "2":
                        await message.channel.send("Ingresa el tema")
                        tema_p = await bot.wait_for('message', check=check, timeout=60)
                        tema = tema_p.content
                        await message.channel.send("Ingresa la documentacion extra")
                        documentacion_extra_p = await bot.wait_for('message', check=check, timeout=60)
                        documentacion_extra = documentacion_extra_p.content
                        await message.channel.send("Ingresa link de la diapositiva")
                        diapositiva_p = await bot.wait_for('message', check=check, timeout=60)
                        diapositiva = diapositiva_p.content
                        await message.channel.send("Ingresa link de la lecture correspondiente")
                        lecture_p = await bot.wait_for('message', check=check, timeout=60)
                        lecture = lecture_p.content
                        await message.channel.send("Ingresa fecha de inicio")
                        fecha_inicio_p = await bot.wait_for('message', check=check, timeout=60)
                        fecha_inicio = fecha_inicio_p.content
                        await message.channel.send("Ingresa link de la lecture correspondiente")
                        fecha_fin_p = await bot.wait_for('message', check=check, timeout=60)
                        fecha_fin = fecha_fin_p.content

                        try:
                            db.execute("""
                                    INSERT INTO semanas(tema, documentacion_extra, diapositivas, lectures, fecha_inicio, fecha_finalizacion) 
                                    VALUES (?, ?, ?, ?, ?, ?)
                                    """, (tema, documentacion_extra, diapositiva, lecture, fecha_inicio, fecha_fin))
                            conn.commit()
                        except Exception as e:
                            print(e)
                        finally:
                            conn.close()

                # match opcion:
                #     case "1":
                #         await message.channel.send(resultados[0])
                #     case "2":
                #         await message.channel.send(resultados[1])
                #     case "3":
                #         await message.channel.send(resultados[2])
                #     case "4":
                #         await message.channel.send(resultados[3])

            elif response.content == '3':
                await message.channel.send("Ingresa el mensaje que quieres enviar al otro canal")
                respuesta = await bot.wait_for('message', check=check, timeout=20)
                mensaje = respuesta.content
                await enviar_notificacion(message, mensaje)

            elif response.content == '2':
                #Verificacion de acceso al comando
                role_names = [role.name for role in message.author.roles]
                if "STAFF" not in role_names:
                    await message.channel.send("No tienes permitido el acceso a este comando ya que no eres STAFF.")
                    return

                #fechas de bloques establecidos
                today_date = dt.datetime.now()
                today_date = today_date.strftime('%Y-%m-%d')
                class_1_start = today_date + " 08:00:00"
                class_1_end = today_date + " 10:00:00"
                class_2_end = today_date + " 12:00:00"
                Office_hours_start = today_date + " 13:00:00"
                Office_hours_end = today_date + " 15:00:00"

                #Eleccion del emoji para la asistencia del bloque de hoy
                await message.channel.send("Elige el emoji de hoy")
                date_command = dt.datetime.now()
                date_sent_command = date_command.strftime('%Y-%m-%d %H:%M:%S') 
                date_sent_command_week = date_command.strftime('%Y-%m-%d') 
                selected_emoji = await bot.wait_for('message', check=check, timeout=10)
                today_emoji = selected_emoji.content
                guild_id = message.guild.id  #obtiene el id del servidor
                guild = await bot.fetch_guild(guild_id) 
                today_staff = await message.guild.fetch_member(message.author.id)
                today_staff = today_staff.nick

                find_me = today_staff.find("-") 
                user_group_field = today_staff[:find_me].strip()
                full_name = today_staff[find_me + 1:].strip()
                parts = full_name.split(" ")
                user_name = parts[0]
                user_lastname = parts[1]

                person = db.execute("SELECT codigo_usuario FROM usuarios WHERE nombre = ? AND apellido = ? AND grupo = ?", (user_name, user_lastname, user_group_field)).fetchone()
                staff_id = person[0]  
                if (date_sent_command >= class_1_start and date_sent_command <= class_1_end) or (date_sent_command >= class_1_end and date_sent_command <= class_2_end):
                    bloque = "Clases"
                        
                elif date_sent_command >= Office_hours_start and date_sent_command <= Office_hours_end:
                    bloque = "Office Hours"

                else:
                    bloque = "Fuera del horario"

                #Reconocimiento de el numero de semana correspondiente
                id_week = 0

                for i in range (10):
                    week_starts = db.execute("SELECT fecha_inicio FROM semanas WHERE id = ?",(i+1,)).fetchone()
                    week_starts = week_starts[0]
                    week_ends = db.execute("SELECT fecha_finalizacion FROM semanas WHERE id = ?",(i+1,)).fetchone()
                    week_ends = week_ends[0]

                    if date_sent_command_week <= week_ends and date_sent_command_week >= week_starts:
                        id_week = i + 1
                        break
                    else:
                        continue

                db.execute("INSERT INTO control_asistencia(responsable,emoji_seleccionado,momento_toma_asistencia,semana_de_asistencia,bloque_de_asistencia) VALUES(?,?,?,?,?)",(staff_id,today_emoji,date_sent_command,id_week,bloque))        
                conn.commit()
                
                #Registro de todas las reacciones
                react_to_ = await message.channel.send("Reacciona a este mensaje") #Se toman las reacciones de este mensaje
                await asyncio.sleep(10)  #tiempo de espera para reaccionar

                react_to_ = await message.channel.fetch_message(react_to_.id) #realiza una llamada asíncrona para recuperar la versión más actualizada del mensaje para tomar asistencia
                reactions = react_to_.reactions   #toma las reacciones registradas en react_to mediante el atributo reactions el cual accede a una lista de instancias de la clase reaction 
                All_reactions = []

                for reaction in reactions:
                    emoji = reaction.emoji
                    date = dt.datetime.now()
                    date = date.strftime('%Y-%m-%d %H:%M:%S')                  
                    users = [user async for user in reaction.users()]
                    
                    for user in users:
                        guild_id = message.guild.id  #obtiene el id del servidor
                        guild = await bot.fetch_guild(guild_id)   #accede al contenido del bot en el server especificado
                        member = await guild.fetch_member(user.id) #accede al contenido del miembro por su id
                        
                        if member.nick is None:
                            await message.channel.send("Nickname no disponible")
                            return 1
                        elif "Grupo" not in member.nick and "STAFF" not in member.nick:
                            await message.channel.send("Nickname no válido")
                            return 1
                        else:
                            nickname = member.nick#obtiene el nickname del miembro en el server

                        dic = {"nickname": nickname, "emoji": emoji, "date": date}
                        All_reactions.append(dic)

                #Anexar datos a la tabla asistencias
                for dic in All_reactions:
                    find_me = dic["nickname"].find("-") 
                    user_group_field = dic["nickname"][:find_me].strip()
                    full_name = dic["nickname"][find_me + 1:].strip()
                    parts = full_name.split(" ")
                    user_name = parts[0]
                    user_lastname = parts[1]

                    if user_group_field != "STAFF":
                        parts = user_group_field.split(" ")
                        user_group = parts[1]
                        person = db.execute("SELECT codigo_usuario FROM usuarios WHERE nombre = ? AND apellido = ? AND grupo = ?", (user_name, user_lastname, user_group)).fetchone()
                        student_id = person[0]

                        e = dic["emoji"]

                        if  e == today_emoji:
                            estado = "Presente" 
                        elif e != today_emoji:
                            estado = "Ausente"


                        if (dic["date"] >= class_1_start and dic["date"] <= class_1_end) or (dic["date"] >= class_1_end and dic["date"] <= class_2_end):
                            bloque = "Clases"
                        
                        elif dic["date"] >= Office_hours_start and dic["date"] <= Office_hours_end:
                            bloque = "Office Hours"

                        else:
                            bloque = "Fuera del horario"
                            estado = "Ausente"

                        db.execute("INSERT INTO asistencia(codigo_estudiante,estado_asistencia,emoji_enviado,momento_envio,bloque) VALUES(?,?,?,?,?)",(student_id,estado,e,date,bloque))        
                        conn.commit()

                        await message.channel.send(f"Estudiante_id: {student_id}\n Estado: {estado}\n Emoji enviado: {e}\n Momento envio: {date}\n bloque: {bloque}\n ")
                            
            elif response.content == '5':    
                current_date = '2023-07-16'
                assignment_date_1 = db.execute("SELECT * FROM tareas WHERE fecha_liberacion <= ? AND fecha_limite >= ? ",(current_date,current_date)).fetchall()
                if assignment_date_1:
                    await message.channel.send(f"Tus tareas: {assignment_date_1[0][1]}, se liberaron {assignment_date_1[0][2]} y se entregan {assignment_date_1[0][3]}")
                else:
                    await message.channel.send("No hay tareas para hoy.")                             
            
            else:
                await message.channel.send("Opción no válida. Inténtalo de nuevo.")
        except asyncio.TimeoutError:
            await message.channel.send("Se agoto el tiempo de espera, gracias por utilizar el bot de consultas oficial de CS50x.ni")


@bot.event
async def on_ready():
    print(f'Has invocado a {bot.user.name}!')

    #Initialize 
    reminder.start()

#Automated reminder function
@tasks.loop(hours=72)
async def reminder():
    channel_name = 'general'
    general_channel = discord.utils.get(bot.get_all_channels(), name=channel_name)
    #current_date = dt.datetime.now()
    #cuurent_date = date_command.strftime('%Y-%m-%d') 
    current_date = '2023-07-16'

    assignment_date_1 = db.execute("SELECT * FROM tareas WHERE fecha_liberacion <= ? AND fecha_limite >= ? ",(current_date,current_date)).fetchall()
    if assignment_date_1:
        await general_channel.send(f"Tus tareas: {assignment_date_1[0][1]}, se liberaron {assignment_date_1[0][2]} y se entregan {assignment_date_1[0][3]}")
    else:
        await general_channel.send("No hay tareas para hoy.")


bot.run("MTE2NTQ1MjMwNDgyNTIwNDkwOA.Gferpz.rS-1a4e-WPRkr-GxpgH4oHm5RAQZjwsyZ5z9GA")