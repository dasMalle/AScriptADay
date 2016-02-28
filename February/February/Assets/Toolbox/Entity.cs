using UnityEngine;
using System.Collections;

public class Entity : ScriptableObject {

    public string Name;
    public int Level = 1;
    public int Health = 2;
    public int Strength = 1;
    public int Magic = 0;
    public int Defense = 0;
    public int Speed = 1;
    public int Damage = 1;
    public int Armor = 0;
    public string Weapon;
    public Vector2 Position;
}
