using System;
using System.Collections.Generic;

class ProgramaVacunas
{
    static void Main()
    {
        // Conjunto de 500 ciudadanos
        HashSet<string> ciudadanos = new HashSet<string>();
        for (int i = 1; i <= 500; i++)
            ciudadanos.Add("Ciudadano " + i);

        // Vacunados con Pfizer (75)
        HashSet<string> pfizer = new HashSet<string>();
        for (int i = 1; i <= 75; i++)
            pfizer.Add("Ciudadano " + i);

        // Vacunados con AstraZeneca (75)
        HashSet<string> astra = new HashSet<string>();
        for (int i = 51; i <= 125; i++)
            astra.Add("Ciudadano " + i);

        // Ambas dosis
        HashSet<string> ambasDosis = new HashSet<string>(pfizer);
        ambasDosis.IntersectWith(astra);

        // Solo Pfizer
        HashSet<string> soloPfizer = new HashSet<string>(pfizer);
        soloPfizer.ExceptWith(astra);

        // Solo AstraZeneca
        HashSet<string> soloAstra = new HashSet<string>(astra);
        soloAstra.ExceptWith(pfizer);

        // No vacunados
        HashSet<string> noVacunados = new HashSet<string>(ciudadanos);
        noVacunados.ExceptWith(pfizer);
        noVacunados.ExceptWith(astra);

        // Mostrar resultados
        Console.WriteLine("No vacunados: " + noVacunados.Count);
        Console.WriteLine("Ambas dosis: " + ambasDosis.Count);
        Console.WriteLine("Solo Pfizer: " + soloPfizer.Count);
        Console.WriteLine("Solo AstraZeneca: " + soloAstra.Count);
    }
}
