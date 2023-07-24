class Worker {
    // Constructor method for the Worker class
    constructor({ name = '', title = '', salary = 0 }) {
        this.name = name;
        this.title = title;
        this.salary = salary;
    }

    // TODO 6: Add getName(), getTitle(), and getSalary() methods

    getName() {
        return this.name;
    }

    getTitle() {
        return this.title;
    }

    getSalary() {
        return this.salary;
    }

}

// Factory function to create a new worker
class WorkerFactory {

    // Method to create a new FryCook, accepts a name
    createFryCook(name) {
        return new Worker({ name, title: 'Fry Cook', salary: salaryRange(25000) });
    }

    // TODO 7: Add createCashier(name) and createManager(name) methods
    
    createCashier(name) {
        return new Worker({ name, title: 'Cashier', salary: salaryRange(20000) });
    }

    createManager(name) {
        return new Worker({ name, title: 'Manager', salary: salaryRange(50000) });
    }

}

function salaryRange(baseSalary) {
    return Math.floor(Math.random() * 10000) + baseSalary;
}

function showEmployees() {
    // clears the entire contents of the div with id="main-content"
    document.getElementById("main-content").innerHTML = "";

    // Create a new WorkerFactory
    const workerFactory = new WorkerFactory();

    // avoiding opening files with XMLHttpRequest or fetch or anything like that because students may not be able to do that yet
    const fryCookNames = ["Yvette Turcotte", "Jackie Swift", "Tyshawn Kilback", "Ford Jast", "Dr. Kristopher Swaniawski", "Darby Satterfield", "Elisabeth Greenholt", "Dr. Elissa Nolan", "Eugene Batz", "Jay Russel", "Ericka Grady", "Ms. Hannah Larkin", "Madaline Mann", "Georgianna Trantow", "Thaddeus Hettinger", "Mrs. Amy Abbott", "Luther Welch", "Toy Casper", "Mrs. Nadia Carter", "Charlie Bartell", "Francesca Hoppe", "Marietta Wiegand II", "Maverick Feeney", "Norene Ward", "Dr. Meggie Hermann", "Dr. Natalia Satterfield", "Mr. Dixie Hilll", "Miss Sally Russel", "Aimee Botsford", "Ruthie Connelly", "Miss Nelle Conroy", "Jaunita Hackett", "Alta Muller", "Stephanie Murphy", "Ms. Lacey Feil", "Dejah Kiehn", "Kaela Heathcote", "Herman Toy", "Pete Kessler", "Graham Klein", "Donnell Beier", "Brennan Stamm IV", "Mrs. Eddie Rutherford", "Constance Considine", "Braden Cormier", "Markus Quitzon", "Gladyce Brakus", "Dennis Bartoletti", "Johann Jerde", "Jamarcus Macejkovic Sr.", "Ashly Glover", "Milan Harris", "Maxine Kilback", "Breana Pfannerstill Jr.", "Luigi Schowalter", "Verla Reinger PhD", "Ms. Susanna Kub", "Maria Bailey", "Murray Okuneva Jr.", "Eriberto Gottlieb", "Erika Abbott", "Jeffrey Kunde", "Kelley Powlowski", "Lemuel Gibson", "Americo Kunde", "Mrs. Shanny Emard", "Gwen Spencer", "Lloyd Koch DVM", "Diamond Bednar", "Walker Schroeder I", "Mr. Christelle McLaughlin", "Gertrude Boyer", "Karson Hegmann", "Penelope Kutch", "Charlotte Blanda", "Edgardo Rath Sr.", "Myrl Gleason", "Ernie Legros", "Adella Schmitt", "Una Zulauf III", "Daniela Strosin", "Abbey Donnelly DVM", "Celestino Pacocha", "Ms. Buford Braun", "Soledad Macejkovic Sr.", "Demetris Johnston", "Verdie Robel", "Mrs. Bruce Schamberger", "Hortense Harris", "Jolie Oberbrunner", "Jazmyne Reichert", "Margot Hudson", "Selmer Thompson", "Clifford Moen", "Austyn Feest", "Josianne Hagenes", "Adrianna Harªann", "Holden Jewess", "Hollis Howe Sr.", "Destiny Torp"];
    const cashierNames = ["Dr. Orie Kub", "Vena Bartoletti", "Madeline Rempel", "Brock Waters", "Marcellus Schimmel", "Herbert Schaden", "Alfredo Wilkinson", "Deondre Guªann", "Chad Wyman", "Graham Ebert Sr.", "Jessie Schulist", "Arlene Medhurst", "Margarett Mraz", "Kaela Cole", "Damian Little", "Palma Kling", "Kory Gislason", "Arvilla Howell IV", "Armand Hammes", "Ms. Malika Hane", "Abraham Green", "Lonie Deckow", "Kameron Harris", "Derrick Leuschke", "Eugene Monahan", "Saige Pfannerstill", "Amira Schuster", "Vella Stamm", "Myrtle Ebert", "Jaylon Johns", "Elouise Toy", "Coy Jacobson", "Carol Hoeger", "Jaylan Kuhic", "Ms. Maxine Howe", "Randi Hermiston", "Crawford Boyle", "Rossie Ward", "Lloyd Koch DVM", "Mrs. Maudie Borer", "Brenna Medhurst", "Hortense Hintz", "Viola Lind", "Dr. Maia Feest", "Felipa Hermiston", "Theo Schinner", "Jarrod Koelpin Sr.", "Pablo Kihn", "Ephraim Kuvalis MD", "Ms. Zita Stanton"];
    const managerNames = ["Ms. Kathlyn Gaylord", "Leo Mertz", "Desmond Beahan", "Adrianna Predovic I", "Kelly Harann MD", "Rachel Doyle", "Dr. Darrell Williamson", "Sandy Hand", "Kianna Terry", "Bettie Fahey", "Dr. Florencio Toy", "Ms. Julian Greenholt", "Jacky White", "Dr. Larry Johnson", "Adah Zulauf", "Ms. Gaetano Jakubowski", "Letha Green", "Kara Abbott", "Garrison Gerhold", "Jaquan Ondricka"];

    // randomly re-order each list of names before collecting them into the allNames array
    fryCookNames.sort(() => Math.random() - 0.5);
    cashierNames.sort(() => Math.random() - 0.5);
    managerNames.sort(() => Math.random() - 0.5);

    var allNames = [fryCookNames, cashierNames, managerNames];

    const table = document.createElement('table');
    const tableHead = document.createElement('thead');
    const row = document.createElement('tr');

    // TODO 8: Create the elements for the `name`, `title`, and `salary` table headers and append them to the `row` element


    tableHead.appendChild(row);
    table.appendChild(tableHead);
    const nameHeader = document.createElement('th');
    nameHeader.textContent = 'Name';
    row.appendChild(nameHeader);

    const titleHeader = document.createElement('th');
    titleHeader.textContent = 'Title';
    row.appendChild(titleHeader);

    const salaryHeader = document.createElement('th');
    salaryHeader.textContent = 'Salary';
    row.appendChild(salaryHeader);

    const tableBody = document.createElement('tbody');

    for (let i = 0; i < 3; i++) {
        name_list = allNames[i];
        var workers = [];
        for (let j = 0; j < name_list.length; j++) {
            let worker;
            if (i == 0) {
                worker = workerFactory.createFryCook(name_list[j]);
                worker_type = "Fry Cooks";
            }
            else if (i == 1) {
                worker = workerFactory.createCashier(name_list[j]);
                worker_type = "Cashiers";
            }
            else {
                worker = workerFactory.createManager(name_list[j]);
                worker_type = "Managers";
            }
            workers.push(worker);
        }

        for (let i = 0; i < workers.length; i++) {
            const row = document.createElement('tr');

            // TODO 9: Create the elements for the `name`, `title`, and `salary` table cells (data) and append them to the `row` element

            const nameCell = document.createElement('td');
            nameCell.textContent = workers[i].getName();
            row.appendChild(nameCell);
        
            const titleCell = document.createElement('td');
            titleCell.textContent = workers[i].getTitle();
            row.appendChild(titleCell);
        
            const salaryCell = document.createElement('td');
            salaryCell.textContent = '$'+" "+workers[i].getSalary().toLocaleString();
            row.appendChild(salaryCell);
        
            tableBody.appendChild(row);

        };
    }
    table.appendChild(tableBody);
    document.getElementById("main-content").appendChild(table);
}

window.onload = function () {
    showEmployees();
}