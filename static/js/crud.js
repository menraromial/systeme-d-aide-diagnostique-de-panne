
  /*$(document).ready(function() {
    // Add task form submission
    $('#panne_form').submit(function(event) {
      event.preventDefault();
      console.log("Typing typing.....")
      $.ajax({
        url: '{% url "search" %}',
        type: 'POST',
        data: $(this).serialize(),
        success: function(response) {
          const sol = response.sol;
          $('#solutions_list').append(
            `<li>${sol.label}</li>`
          );
          $('#panne_form')[0].reset();
        },
        error: function(xhr, status, error) {
          console.error(error);
        }
      });
    });

    // Delete task button click
    /*$('#task-list').on('click', '.delete-task', function() {
      const task_id = $(this).closest('li').data('task-id');
      $.ajax({
        url: `/delete-task/${task_id}/`,
        type: 'POST',
        data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function(response) {
          $(`li[data-task-id="${task_id}"]`).remove();
        },
        error: function(xhr, status, error) {
          console.error(error);
        }
      });
    });
  });*/


  document.addEventListener('DOMContentLoaded', function() {
    // Add task form submission
    const addTaskForm = document.querySelector('#panne_form');
    addTaskForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const formData = new FormData(addTaskForm);
      fetch('search/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        const sol = data.sol;
        console.log(sol.context)
        const taskList = document.querySelector('#solutions_list');
        taskList.innerHTML=""
        //taskList.reset()
        const newTask = document.createElement('li');
        //newTask.setAttribute('data-task-id', task.id);
        newTask.innerHTML = `${sol.label}`;
        taskList.appendChild(newTask);

        //Ajout des solutions
        const solutions = sol.context.solutions;
        const sol_list = document.getElementById('solutions');
        sol_list.innerHTML=""
        solutions.forEach(item => {
          const li = document.createElement('li');
          li.innerHTML = item;
          sol_list.appendChild(li);
        });

        // Ajout des composants
        const composants = sol.context.composant;
        const c_list = document.getElementById('composants');
        c_list.innerHTML=""
        composants.forEach(item => {
          const li = document.createElement('li');
          li.innerHTML = item;
          c_list.appendChild(li);
        });

        //Ajout des marques
        const marques = sol.context.marques;
        const m_list = document.getElementById('marques');
        m_list.innerHTML=""
        marques.forEach(item => {
          const li = document.createElement('li');
          li.innerHTML = item;
          m_list.appendChild(li);
        });

        addTaskForm.reset();
      })
      .catch(error => console.error(error));
    });

  });



