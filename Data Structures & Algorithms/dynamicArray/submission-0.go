type DynamicArray struct {
    arr      []int
    size     int
    capacity int
}

func NewDynamicArray(capacity int) *DynamicArray {
    if capacity <= 0 {
        capacity = 1
    }

    return &DynamicArray{
        arr:      make([]int, capacity),
        size:     0,
        capacity: capacity,
    }
}

func (da *DynamicArray) Get(i int) int {
    if i < 0 || i >= da.size {
        panic("index out of range")
    }

    return da.arr[i]
}

func (da *DynamicArray) Set(i int, n int) {
    if i < 0 || i >= da.size {
        panic("index out of range")
    }

    da.arr[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    if da.size == da.capacity {
        da.resize()
    }

    da.arr[da.size] = n 
    da.size++
}

func (da *DynamicArray) Popback() int {
    if da.size == 0 {
        panic("array is empty")
    }

    da.size--
    value := da.arr[da.size]
    da.arr[da.size] = 0

    return value
}

func (da *DynamicArray) resize() {
    newCapacity := da.capacity * 2
    newArr := make([]int, newCapacity)

    for i := 0; i < da.size; i++ {
        newArr[i] = da.arr[i]
    }

    da.arr = newArr
    da.capacity = newCapacity
}

func (da *DynamicArray) GetSize() int {
	return da.size
}

func (da *DynamicArray) GetCapacity() int {
	return da.capacity
}
