"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Server:
    """Parent class that represents a basic computer server."""

    device_type = "General Server"

    def __init__(self, hostname, memory_gb):
        # Handle a missing hostname with a safe default value.
        self.hostname = hostname if hostname else "unnamed-server"

        # Invalid memory values are rejected so the object is not created
        # with an impossible amount of memory.
        if not isinstance(memory_gb, int) or memory_gb <= 0:
            raise ValueError("memory_gb must be a positive integer")

        self.memory_gb = memory_gb

    def display_info(self):
        """Display the basic information stored in this server object."""
        print(
            f"Hostname: {self.hostname}, "
            f"Memory: {self.memory_gb} GB, "
            f"Type: {self.device_type}"
        )

    def has_enough_memory(self, required_gb):
        """Return True when the server meets a requested memory amount."""
        return self.memory_gb >= required_gb


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class CloudServer(Server):
    """Child class that extends Server with cloud-specific information."""

    provider = "Private Cloud"

    def __init__(self, hostname, memory_gb, region, server_id):
        # Reuse the parent constructor for hostname and memory.
        super().__init__(hostname, memory_gb)
        self.region = region
        self.server_id = server_id

        # Each CloudServer receives its own mutable list.
        # The list stores dictionaries so the data is nested and mutable.
        self.services = []

    def add_service(self, service_name, ports=None):
        """Add a service and its port list to this cloud server."""
        if not service_name:
            raise ValueError("service_name cannot be empty")

        if ports is None:
            ports = []

        self.services.append({
            "name": service_name,
            "ports": list(ports)
        })

    def display_info(self):
        """Override Server.display_info with cloud-specific information."""
        service_names = [service["name"] for service in self.services]
        print(
            f"Hostname: {self.hostname}, "
            f"Memory: {self.memory_gb} GB, "
            f"Provider: {self.provider}, "
            f"Region: {self.region}, "
            f"Server ID: {self.server_id}, "
            f"Services: {service_names}"
        )

    # Student-created extension:
    # __len__ lets len(cloud_server) report how many services are installed.
    def __len__(self):
        return len(self.services)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    server_one = CloudServer("web-01", 32, "eu-central", "CS-101")
    server_two = CloudServer("db-01", 64, "us-east", "CS-102")

    # Access the class variable directly through the class.
    print("Class variable through CloudServer:", CloudServer.provider)

    # Access the same class variable through an instance.
    print("Class variable through server_one:", server_one.provider)

    # This attribute is added only to server_one's instance namespace.
    server_one.maintenance_window = "Sunday 02:00"

    print("\nserver_one instance namespace:")
    print(server_one.__dict__)

    print("\nserver_two instance namespace:")
    print(server_two.__dict__)

    # Class data and methods are stored in the class namespace rather than
    # being duplicated inside every object's instance namespace.
    visible_class_names = [
        name for name in CloudServer.__dict__
        if not name.startswith("__")
    ]
    print("\nCloudServer class namespace entries:")
    print(visible_class_names)
    print("CloudServer.provider from class namespace:", CloudServer.__dict__["provider"])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = CloudServer("app-01", 48, "eu-west", "CS-201")
    original.add_service("Database", [3306])
    original.add_service("Web API", [443])

    shallow = copy(original)
    deep = deepcopy(original)

    # A shallow copy creates a new CloudServer object, but the nested
    # services list is still referenced by both original and shallow.
    #
    # A deep copy creates a new CloudServer object and recursively copies
    # the nested mutable data, so its services can change independently.
    original.services[0]["ports"].append(5432)
    original.services.append({"name": "Monitoring", "ports": [9090]})

    print("Original services:", original.services)
    print("Shallow copy services:", shallow.services)
    print("Deep copy services:", deep.services)

    print(
        "Original and shallow share the services list:",
        original.services is shallow.services
    )
    print(
        "Original and deep share the services list:",
        original.services is deep.services
    )


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object Demonstration ===")
    parent_server = Server("local-01", 16)
    parent_server.display_info()

    # Additional edge-case test: a missing hostname is replaced with a
    # readable default rather than leaving the object with an empty name.
    unnamed_server = Server("", 8)
    print("Missing-hostname edge case:")
    unnamed_server.display_info()

    print("\n=== Child Object Demonstration ===")
    child_server = CloudServer("cloud-01", 64, "eu-central", "CS-001")
    child_server.add_service("Web Server", [80, 443])
    child_server.add_service("Database", [3306])
    child_server.display_info()

    # The child object inherits has_enough_memory() from Server.
    print(
        "Inherited memory check (needs 32 GB):",
        child_server.has_enough_memory(32)
    )

    # Student-created __len__ extension.
    print("Installed service count using len():", len(child_server))

    # Additional invalid-input test with graceful error handling.
    try:
        child_server.add_service("")
    except ValueError as error:
        print("Handled invalid service name:", error)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
