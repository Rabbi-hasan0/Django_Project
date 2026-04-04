from django.shortcuts import render, redirect
import requests
from datetime import datetime
from .models import Post
from .common_function import checkUserPermission
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if not checkUserPermission(request, "can_view", "/blog"):
        return render(request, 'blog/permission_denied.html')
    
    posts=Post.objects.all()
    contex = {
        'posts': posts
    }

    return render(request, 'blog/home.html', contex)

    
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})









































def dashboard_view(request):
    handle = request.GET.get('handle')
    context = {'handle': handle, 'success': False}

    if handle:
        # API URLs
        info_url = f"https://codeforces.com/api/user.info?handles={handle}"
        # count=10000 deya hoyeche jate shob submission ashe (shudhu last 1-2 bochhorer noy)
        status_url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=10000"
        
        try:
            info_res = requests.get(info_url).json()
            status_res = requests.get(status_url).json()
            
            if info_res['status'] == 'OK' and status_res['status'] == 'OK':
                user_info = info_res['result'][0]
                submissions = status_res['result']
                
                rating_counts = {}
                daily_activity = {}
                unique_solved = set()

                for sub in submissions:
                    # Unix timestamp theke date ber kora
                    dt = datetime.fromtimestamp(sub['creationTimeSeconds'])
                    date_str = dt.strftime('%Y-%m-%d')
                    
                    # Proti diner activity count (shob bochhorer jonno)
                    daily_activity[date_str] = daily_activity.get(date_str, 0) + 1
                    
                    # Solved problem logic
                    if sub.get('verdict') == 'OK':
                        p_id = f"{sub['problem'].get('contestId')}{sub['problem'].get('index')}"
                        if p_id not in unique_solved:
                            unique_solved.add(p_id)
                            r = sub['problem'].get('rating')
                            if r:
                                rating_counts[r] = rating_counts.get(r, 0) + 1

                sorted_ratings = sorted(rating_counts.keys())
                
                # Heatmap data format: [Year, Month-1, Day, Count]
                heatmap_data = []
                for date, c in daily_activity.items():
                    y, m, d = map(int, date.split('-'))
                    heatmap_data.append([y, m-1, d, c])

                context.update({
                    'user': user_info,
                    'ratings': sorted_ratings,
                    'counts': [rating_counts[r] for r in sorted_ratings],
                    'heatmap_data': heatmap_data,
                    'total_solved': len(unique_solved),
                    'success': True
                })
            else:
                context['error_message'] = "User not found."
        except Exception as e:
            context['error_message'] = f"Error: {str(e)}"
            
    return render(request, 'activity.html', context)

