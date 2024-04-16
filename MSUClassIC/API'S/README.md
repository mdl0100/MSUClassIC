# Backend

## API Endpoints

1. Department
   - `GET` /api/department
   - `POST` /api/department
2. Axis
   - `POST` /api/axis
3. Schedule
   - `POST` /api/schedule



## Examples

1. Add a new department

   ```js
   axios.post("http://127.0.0.1:8000/api/department/", {
     name: "Department Name",
   });
   ```

2. Add a new axis

   ```js
   axios.post("http://127.0.0.1:8000/api/axis/", {
     department: {
       name: "Department Name",
     },
     x: 2,
     y: 0,
     width: 2,
     height: 1,
     name: "Axis Name",
     static: true,
     moved: false,
   });
   ```

3. Add a new schedule

   ```js
   axios.post("http://127.0.0.1:8000/api/schedule/", {
     department: {
       name: "Department Name",
     },
     x: 4,
     y: 3,
     width: 4,
     height: 7,
     name: "Class Name",
     static: false,
     moved: false,
   });
   ```

4. Get All Schedules by Department

   ```js
   axios.get("http://127.0.0.1:8000/api/department/<department_id>/");
   ```

   ```json
   // Example
   // http://127.0.0.1:8000/api/department/3/

   // Output
   {
     "department": {
       "id": 3,
       "name": "Test2"
     },
     "axis": [
       {
         "id": 2,
         "department": {
           "id": 3,
           "name": "Test2"
         },
         "x": 2,
         "y": 0,
         "width": 2,
         "height": 1,
         "name": "Test2",
         "static": true,
         "moved": false
       }
     ],
     "schedule": [
       {
         "id": 2,
         "department": {
           "id": 3,
           "name": "Test2"
         },
         "x": 1,
         "y": 1,
         "width": 1,
         "height": 1,
         "name": "Test",
         "static": false,
         "moved": false
       }
     ]
   }
   ```

5. Delete Schedule

   ```js
   axios.delete("http://127.0.0.1:8000/api/schedule/delete/<schedule_id>/");
   ```
