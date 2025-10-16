// API base URL - adjust according to your backend
const API_BASE_URL = '';

// DOM Elements
const ticketForm = document.getElementById('ticketForm');
const responseContainer = document.getElementById('responseContainer');
const ticketList = document.getElementById('ticketList');

// Event Listeners
ticketForm.addEventListener('submit', handleTicketSubmit);

// Handle ticket submission
async function handleTicketSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const formData = new FormData(ticketForm);
    const ticketData = {
        subject: formData.get('subject'),
        description: formData.get('description'),
        priority: formData.get('priority')
    };
    
    try {
        // Show loading state
        responseContainer.innerHTML = '<p>Processing your ticket with AI...</p>';
        responseContainer.className = 'loading';
        
        // Add loading state to button
        const submitButton = ticketForm.querySelector('button');
        const originalButtonText = submitButton.textContent;
        submitButton.textContent = 'Processing...';
        submitButton.disabled = true;
        submitButton.classList.add('loading');
        
        // Submit ticket
        const ticketResponse = await submitTicket(ticketData);
        
        // Get AI response
        const aiResponse = await getAIResponse(ticketData.description);
        
        // Display AI response
        displayAIResponse(aiResponse.response);
        
        // Refresh ticket list
        await loadTicketHistory();
        
        // Reset form
        ticketForm.reset();
        
        // Restore button state
        submitButton.textContent = originalButtonText;
        submitButton.disabled = false;
        submitButton.classList.remove('loading');
        
    } catch (error) {
        console.error('Error:', error);
        responseContainer.innerHTML = '<p class="error">Error processing your request. Please try again.</p>';
        responseContainer.className = '';
        
        // Restore button state
        const submitButton = ticketForm.querySelector('button');
        submitButton.textContent = 'Submit Ticket';
        submitButton.disabled = false;
        submitButton.classList.remove('loading');
    }
}

// Submit ticket to backend
async function submitTicket(ticketData) {
    const response = await fetch(`${API_BASE_URL}/api/tickets`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(ticketData),
    });
    
    if (!response.ok) {
        throw new Error('Failed to submit ticket');
    }
    
    return response.json();
}

// Get AI response
async function getAIResponse(query) {
    const response = await fetch(`${API_BASE_URL}/api/ai/respond`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    });
    
    if (!response.ok) {
        throw new Error('Failed to get AI response');
    }
    
    return response.json();
}

// Display AI response
function displayAIResponse(response) {
    responseContainer.innerHTML = `
        <div class="ai-response-content">
            <h3>AI Assistant Response:</h3>
            <p>${response}</p>
        </div>
    `;
    responseContainer.className = ''; // Remove loading class
}

// Load ticket history
async function loadTicketHistory() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/tickets`);
        
        if (!response.ok) {
            throw new Error('Failed to load tickets');
        }
        
        const data = await response.json();
        displayTicketHistory(data.tickets);
        
    } catch (error) {
        console.error('Error loading tickets:', error);
        ticketList.innerHTML = '<p class="error">Error loading ticket history.</p>';
    }
}

// Display ticket history
function displayTicketHistory(tickets) {
    if (!tickets || tickets.length === 0) {
        ticketList.innerHTML = '<p>No tickets found. Submit your first ticket!</p>';
        return;
    }
    
    const ticketsHTML = tickets.map(ticket => `
        <div class="ticket-item">
            <h4>${ticket.subject}</h4>
            <p>${ticket.description}</p>
            <span class="priority ${ticket.priority}">${ticket.priority}</span>
        </div>
    `).join('');
    
    ticketList.innerHTML = ticketsHTML;
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    loadTicketHistory();
});