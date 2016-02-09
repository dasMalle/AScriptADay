using UnityEngine;
using System.Collections;
using UnityEditor;

[CustomEditor(typeof(AsteroidSpawn))]
public class AstroidEditor : Editor {

    public override void OnInspectorGUI()
    {
        AsteroidSpawn myTarget = (AsteroidSpawn)target;
        EditorGUILayout.IntField("AsteroidsInScene", myTarget.AsteroidCount());
    }

}
