class GenerateCombinationExerciseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        exercise_type_id = request.data.get('exercise_type_id')

        try:
            exercise_type = ExerciseType.objects.get(id=exercise_type_id)
        except ExerciseType.DoesNotExist:
            return Response(
                {'error': 'Übungstyp nicht gefunden.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Erstelle eine neue Übung
        exercise = Exercise.objects.create(user=user, exercise_type=exercise_type)

        # Wähle zufällige Wörter für die Übung aus
        conjunctions = GermanWord.objects.filter(user=user, word_class='CONJ')
        adjectives = GermanWord.objects.filter(user=user, word_class='ADJ')
        pronouns = GermanWord.objects.filter(user=user, word_class='PRON')

        if not conjunctions.exists() or not adjectives.exists() or not pronouns.exists():
            return Response(
                {'error': 'Nicht genügend Wörter für die Übung gefunden.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generiere Übungsaufgaben
        for _ in range(5):  # Maximal 5 Aufgaben
            conjunction = random.choice(conjunctions)
            adjective = random.choice(adjectives)
            pronoun = random.choice(pronouns)

            question = f"Bilde einen Satz mit: {conjunction.base_form}, {adjective.base_form}, {pronoun.base_form}"
            correct_answer = f"{conjunction.base_form} {adjective.base_form} {pronoun.base_form} ..."  # Beispielantwort

            ExerciseItem.objects.create(
                exercise=exercise,
                word=conjunction,  # Wir speichern nur ein Wort, aber die Frage bezieht sich auf alle
                question=question,
                correct_answer=correct_answer
            )

        # Serialisiere die Übung für die Antwort
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_201_CREATED)