// IM Silly Sentences
#include <stdio.h>
#include <string.h>

int main(){
    char name[50];
    char place[50];
    char verb[50];
    char adj[50];
    char noun[50];

    printf("Type a name: ");
    scanf("%s", &name);

    printf("Type a place: ");
    scanf("%s", &place);

    printf("Type verb: ");
    scanf("%s", &verb);

    printf("Type an adjictive:");
    scanf("%s", &adj);

    printf("Type a noun: ");
    scanf("%s", &noun);
    
    strcat(adj, " ");
    strcat(adj, noun);

    printf("%s went to %s where they %s and bought a %s", name, place, verb, adj);

    return 0;
}