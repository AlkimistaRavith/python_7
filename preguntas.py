preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuál dios habita en el Monte Olimpo?'],
    'alternativas': [['Ra', 0], 
                     ['Zeus', 1], 
                     ['Hades', 0], 
                     ['Odin', 0]]},
    'pregunta_2': {'enunciado':['¿Cuál dios fue faraon por 1000 años?'],
    'alternativas': [['Odin', 0], 
                     ['Seth', 0], 
                     ['Zeus', 0], 
                     ['Ra', 1]]},
    
    'pregunta_3': {'enunciado':['¿Qué dios tiene 2 cuervos ayudantes y vive en Asgard?'],
    'alternativas': [['Zeus', 0], 
                     ['Ra', 0], 
                     ['Odin', 1], 
                     ['Loki', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['¿A quien le pertenece el martillo de Mjolnir?'],
    'alternativas': [['Odin', 0], 
                     ['Thor', 1], 
                     ['Loki', 0], 
                     ['Heimdall', 0]]},
    'pregunta_2': {'enunciado':['En la mitología griega, ¿Quién es el dios del inframundo?'],
    'alternativas': [['Hades', 1],
                     ['Zeus', 0], 
                     ['Ares', 0], 
                     ['Poseidon', 0]]},
    
    'pregunta_3': {'enunciado':['En la mitología egipcia, ¿Quien era la diosa de la maternidad, la magia y la protección?'],
    'alternativas': [['Bastet', 0], 
                     ['Isis', 1], 
                     ['Uadjet', 0], 
                     ['Ptah', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['En la mitología griega, ¿Quien fue Calisto?'],
    'alternativas': [['Sacerdotiza de Atenea, quien se acostó con Poseidon en el templo de Atenea y fue castigada y transformada en Medusa.', 0], 
                     ['Cazadora del cortejo de Artemisa, quien fue engañada por Zeus transformado en Artemisa, para acostarse con ella. De castigo fue transformada en osa, y Zeus la convirtió en la constelación de la Osa Mayor.', 1], 
                     ['Hija de Demeter, raptada por Hades para ser su esposa. Aunque fue devuelta, debe pasar 6 meses en el Inframundo, para cumplir su voto de esposa.', 0], 
                     ['Esposa de Anfitrión, quien fue engañada y embarazada por Zeus, dando a luz al semidios Heracles (o Hércules).', 0]]},
    'pregunta_2': {'enunciado':['Luego de su retiro como faraon, Ra dios del Sol, se enfrenta cada noche a una bestia que representa la oscuridad y el caos cósmico. ¿Quién es esta bestia?'],
    'alternativas': [['El escarabajo Khepri', 0], 
                     ['El ave fénix Bennu.', 0], 
                     ['La serpiente gigante Apofis', 1], 
                     ['La criatura infernal Ammit.', 0]]},
    
    'pregunta_3': {'enunciado':['En la mitología nordica, ¿Cómo se llaman los 2 cuervos de Odin, que representan el pensamiento y la memoria.'],
    'alternativas': [['Fenrir y Jormungandr', 0], 
                     ['Hugin y Munin.', 1], 
                     ['Tanngrisnir y Tanngnjóstr', 0], 
                     ['Geri y Freki', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}