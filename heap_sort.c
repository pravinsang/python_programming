#include<stdio.h>
int heap_size, arr_length;
void swap(int *p, int *q)
{
    int temp;
    temp = *p;
    *p = *q;
    *q = temp; 
}
void max_heapify(int a[],int i)
{
    int l,r,largest;
    l = 2 * i + 1;
    r = 2 * i + 2;
    if(l <= heap_size && a[l]>a[i])
        largest = l;
    else
        largest = i;
    if(r <= heap_size && a[r]>a[largest])
        largest = r;
    if(largest != i)
    {
        swap(&a[i],&a[largest]);
        max_heapify(a,largest);
    }
}
void build_max_heap(int a[])
{
    heap_size = arr_length - 1;
    for(int i = (arr_length/2) - 1; i>= 0; i--)
        max_heapify(a,i);
}
void heap_sort(int a[])
{
    build_max_heap(a);
    for(int i=arr_length-1 ;i>=1; i--)
    {
        swap(&a[0],&a[i]);
        heap_size--;
        max_heapify(a,0);
    }
}
int main()
{
    int a[]={3, 4, 10, 1, 12, 6};
    arr_length = sizeof(a)/sizeof(int);
    heap_sort(a);
    printf("The elements are: ");
    for(int i=0; i<arr_length; i++)
        printf("%d ",a[i]);
    return 0;
}