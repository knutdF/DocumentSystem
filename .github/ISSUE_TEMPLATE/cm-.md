<!DOCTYPE html>
<html>
<head>
    <title>Change Management Formular</title>
</head>
<body>

    <h2>Change Management Anfrageformular</h2>

    <form action="/submit-your-form-endpoint" method="post">
        <label for="title">Titel der Änderungsanfrage:</label><br>
        <input type="text" id="title" name="title"><br>

        <label for="description">Beschreibung der Änderung:</label><br>
        <textarea id="description" name="description"></textarea><br>

        <label for="reason">Begründung für die Änderung:</label><br>
        <textarea id="reason" name="reason"></textarea><br>

        <label for="impact">Erwartete Auswirkungen:</label><br>
        <textarea id="impact" name="impact"></textarea><br>

        <label for="additionalInfo">Zusätzliche Informationen:</label><br>
        <textarea id="additionalInfo" name="additionalInfo"></textarea><br>

        <input type="submit" value="Anfrage senden">
    </form>

</body>
</html>

