#include <iostream>
using namespace std;

void merge(int arr[], int l, int mid, int r){
    int n1 = mid - l + 1;
    int n2 = r - mid;
    
    int a[n1];
    int b[n2]; // temporary arrays
    
    for(int i=0;i<n1;i++){
        a[i] = arr[l+i];
    }
    for(int i=0;i<n2;i++){
        b[i] = arr[mid+1+i];
    }
    
    int i=0; // pointer for a array
    int j=0; // pointer for b array
    int k=l; // for traversing the array
    
    while(i<n1 && j<n2){
        if(a[i] < b[j]){
            arr[k] = a[i];
            k++; i++;
        }
        else{
            arr[k] = b[j];
            k++; j++;
        }
    }
//    case: if one of the pointer reaches the last index while traversing and other havent reached the last pointer, for that we will simply add the remaining values into the array
    
    while(i < n1){
        arr[k] = a[i];
        k++; i++;
    }
    while(j < n2){
        arr[k] = b[j];
        k++; j++;
    }
}

void mergesort(int arr[], int l, int r){
    
    if(l < r){ // if l = r that means we have only 1 element left in an array
        int mid = (l + r)/2;
        mergesort(arr, l, mid);
        mergesort(arr, mid+1, r);
        
        merge(arr, l, mid, r);
        
    }
}

int main(int argc, const char * argv[]) {
    
    int n;
    cout<<"Enter the size of array: ";
    cin>>n;
    
    int arr[n];
    cout<<"Enter "<<n<<" elements in array: "<<endl;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    mergesort(arr, 0, n-1);
    for(int i=n;i>0;i--){
        cout<<arr[i]<<" ";
    }cout<<endl;
    
    return 0;
}